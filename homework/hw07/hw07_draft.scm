; ; (define (interleave first second)
; ;   (if (null? first) second)
; ;   (if (null? second) first)
; ;   (append (list (car first) (car second)) (interleave (cdr first) (cdr second)))
; ; )

; (define (interleave first second)
; (cond 
;     ((null? first) second)
;     ((null? second) first)
;     (else (append (list (car first) (car second)) (interleave (cdr first) (cdr second))))
; )
; )

; (interleave (list 1 3 5) (list 2 4 6))
; ; expect (1 2 3 4 5 6)

; (interleave (list 1 3 5) nil)
; ; expect (1 3 5)

; (interleave (list 1 3 5) (list 2 4))
; ; expect (1 2 3 4 5)

; ; (append (list (car '(1 2 3)) (car '(3 4 5))) '(7 9)) 


; (define (accumulate combiner start n term)
; (if (<= start n)
; (combiner (term start)  (accumulate combiner (+ 1 start) n term)))
; (start - 1)
; )

; (define (accumulate combiner start n term)
;     (define (fun combiner n term)
;     (if(= n 1) (term n) (combiner (term n) (fun combiner (- n 1) term)))
;     )
; (combiner start (fun combiner n term))
; )


; (define (fun combiner n term)
; (if(= n 1) (term n) (combiner (term n) (fun combiner (- n 1) term)))
; )

; (define (identity x) x)

; (define (square x) (* x x))

; (fun * 5 identity)

; (fun + 5 square)

; (accumulate * 1 5 identity)
; (print (accumulate + 0 5 square))
; (print (accumulate + 5 5 square))


; (lambda (x y) (= x y))

; (lambda (x y) (not (= x y))) 


; (define (filter-lst fn lst)
;   (if (null? lst)
;     nil
;     (if (fn (car lst))
;         (append (list (car lst)) (filter-lst fn (cdr lst)))
;         (filter-lst fn (cdr lst))
;         )
;     )
; )


; (define (not_equal x y) ((not (= x y))))

; 判断是否在list里面


; (print (in_list 10 '(0 1 2)))

; (define (no-repeats lst)
;   (define (in_list arg0 lst)
;   (if (null? lst) #f (or ((lambda (x y) (= x y)) arg0 (car lst)) (in_list arg0 (cdr lst))))
;   )
;   (cond 
;   ((null? lst) lst)
;   ((null? (cdr lst)) lst)
;   (else (if (in_list (car lst) (cdr lst))
;   (no-repeats (cdr lst))
;   (append (list (car lst)) (no-repeats (cdr lst)))
;   ))
;   )
; )
