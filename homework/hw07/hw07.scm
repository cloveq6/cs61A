(define (filter-lst fn lst)
  (if (null? lst)
    nil
    (if (fn (car lst))
        (append (list (car lst)) (filter-lst fn (cdr lst)))
        (filter-lst fn (cdr lst))
        )
    )
)

;;; Tests
(define (even? x)
  (= (modulo x 2) 0))
(filter-lst even? '(0 1 1 2 3 5 8))
; expect (0 2 8)


(define (interleave first second)
  (cond 
    ((null? first) second)
    ((null? second) first)
    (else (append (list (car first) (car second)) (interleave (cdr first) (cdr second))))
)
)

(interleave (list 1 3 5) (list 2 4 6))
; expect (1 2 3 4 5 6)

(interleave (list 1 3 5) nil)
; expect (1 3 5)

(interleave (list 1 3 5) (list 2 4))
; expect (1 2 3 4 5)


(define (accumulate combiner start n term)
  (define (fun combiner n term)
    (if(= n 1) (term n) (combiner (term n) (fun combiner (- n 1) term)))
    )
  (combiner start (fun combiner n term))
)


(define (no-repeats lst)
  (define (in_list arg0 lst)
  (if (null? lst) #f (or ((lambda (x y) (= x y)) arg0 (car lst)) (in_list arg0 (cdr lst))))
  )
  (cond 
  ((null? lst) lst)
  ((null? (cdr lst)) lst)
  (else (if (in_list (car lst) (cdr lst))
  (no-repeats (cdr lst))
  (append (list (car lst)) (no-repeats (cdr lst)))
  ))
  )
)

