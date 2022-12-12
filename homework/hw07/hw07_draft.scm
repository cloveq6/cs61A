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




; (define (enumerate s)
;   ; BEGIN PROBLEM 15
;   (define (enumerate-from n remainder-s) (
;     (cond ((null? remainder-s) remainder-s)
;           (else (cons '(n (car remainder-s)) (enumerate-from (+ n 1) (cdr remainder-s))))
;     )
    
;     )
;   )
;   (enumerate-from 0 s)
; )

; (define (fun lst)
; (if (null? lst) (print lst) 
; (begin ((print (car lst)) (fun (cdr lst)) )))
; )

; (define (fun n lst)
; (if (null? lst) lst (begin (print (list n (car lst))) (fun (+ n 1) (cdr lst))))
; )


; (define (enumerate s)
;   ; BEGIN PROBLEM 15
;   (define (enumerate_from n remainder_s) (
;     (if(null? remainder_s) '(1 2))
;     )
;   )
;   (print (enumerate_from 0 s))
; )

; (enumerate '())



; (define (bobo a)
; (define (todou b) (print b)
; )
; (todou a)
; )

; (bobo 1)

; (define (funny lst) (null? lst) lst)
; (funny '())
; (print (funny '()))


; sheme15

; (define (square x) x)


; (define (sum lst) (begin (car lst) (square (cdr lst))))


; (sum '(1 2))


; (define (construct n lst) (if (null? lst) lst (cons (list n (car lst)) (construct (+ n 1) (cdr lst)))))

; (print (construct 0 '(3 4 5 6)))

; (define (enumerate lst)
; (construct 0 lst)
; )

; (print (enumerate '(3 4 5 6)))

; scheme 16




; (define (apply operator a b) (operator a b))

; (apply - 3 2)

; (define (interleave first second)
;   (cond 
;     ((null? first) second)
;     ((null? second) first)
;     (else (append (list (car first) (car second)) (interleave (cdr first) (cdr second))))
; )
; )

; (if (comp (car first) (car second)) (append (list (car first) (fun))) (append (list (car second)) (fun)))


; (define (merge comp list1 list2)
;   (cond
;     ((null? list1) list2)
;     ((null? list2) list1)
;     (else (if (comp (car list1) (car list2)) 
;     (cons (car list1) (merge comp (cdr list1) list2)) 
;     (cons (car list2) (merge comp list1 (cdr list2)))
;     )) 
;     )
;   )
  

;   (merge < '(1 5 7 9) '(4 8 10))

; (cons (cons 1 (car '((2) (3)))) (cdr '((2) (3))))

; (cons (cons (car s) (car (nondecreaselist (cdr s)))) (cdr (nondecreaselist (cdr s))))

; scheme 17
; (define (nondecreaselist s)
;     ; BEGIN PROBLEM 17
;     (cond
;     (null? s)
;     (null? (cdr s) (list s))
;     ((= 0 0) (print 'tt))
;     (else
;     (if (>= (cadr s) (car s)) ((cons (cons (car s) (car (nondecreaselist (cdr s)))) (cdr (nondecreaselist (cdr s))))) 
;     (cons (list (car s) (nondecreaselist (cdr s))))
;     )
;     )
;     ))


; (print (nondecreaselist '(1)))
; (nondecreaselist '(1 2))
; (nondecreaselist '(1 2 3 1))

    ; END PROBLEM 17


; (define (nondecreaselist s) 
; (cond ((null? s) s)
;       ((null? (cdr s)) (list s))
;           (else
;     (if (>= (cadr s) (car s)) (cons (cons (car s) (car (nondecreaselist (cdr s)))) (cdr (nondecreaselist (cdr s))))
;     (cons (list (car s)) (nondecreaselist (cdr s))))
;       )
; )
; )

; (nondecreaselist '(1))

; scheme extra

; (1 2)

; (() ())

; ((1) (2))

; scm> (zip '((1 2) (3 4) (5 6)))
; ((1 3 5) (2 4 6))
; scm> (zip '((1 2)))
; ((1) (2))
; scm> (zip '())
; (() ())

(define (zip pairs)
  (cond ((null? pairs) (list '() '()))
  (else (list (cons (car (car pairs)) (car (zip (cdr pairs)))) (cons (cadr (car pairs)) (cadr (zip (cdr pairs))))))
  )
)
  
;   )


; (define (fun x) (+ x 1))

; (map fun '(1 2 3))

; (list (cons 1 (car '(() ()))) (cons 2(cadr '(() ()))))


; (list (cons 1 (car xx)) (cons 2(cadr xx)))


;; Problem EC
;; Returns a function that checks if an expression is the special form FORM

(define (caar x) (car (car x)))
(define (cadr x) (car (cdr x)))
(define (cdar x) (cdr (car x)))
(define (cddr x) (cdr (cdr x)))


(define (check-special form)
  (lambda (expr) (equal? form (car expr))))

(define lambda? (check-special 'lambda))
(define define? (check-special 'define))
(define quoted? (check-special 'quote))
(define let?    (check-special 'let))

; (define? '(define (x) (+ x 1)))


scm> (let-to-lambda '(let ((a 1) (b 2)) (+ a b)))
((lambda (a b) (+ a b)) 1 2)
scm> (let-to-lambda '(let ((a 1)) (let ((b a)) b)))
((lambda (a) ((lambda (b) b) a)) 1)

;; Converts all let special forms in EXPR into equivalent forms using lambda
(define (let-to-lambda expr)
  (cond ((atom? expr)
         ; BEGIN PROBLEM EC
         expr
         ; END PROBLEM EC
         )
        ((quoted? expr)
         ; BEGIN PROBLEM EC
         'replace-this-line
         ; END PROBLEM EC
         )
        ((or (lambda? expr)
             (define? expr))
         (let ((form   (car expr))
               (params (cadr expr))
               (body   (cddr expr)))
           ; BEGIN PROBLEM EC
           'replace-this-line
           ; END PROBLEM EC
           ))
        ((let? expr)
         (let ((values (cadr expr))
               (body   (cddr expr)))
           ; BEGIN PROBLEM EC
           'replace-this-line
           ; END PROBLEM EC
           ))
        (else
         ; BEGIN PROBLEM EC
         'replace-this-line
         ; END PROBLEM EC
         )))


