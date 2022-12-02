(define (cddr s)
  (cdr (cdr s)))

(define (cadr s)
  (car (cdr s))
)

(define (caddr s)
  (car (cdr (cdr s)))
)


(define (sign num)
  (cond ((> num 0) 1) ((< num 0) -1) (else 0))
)


(define (square x) (* x x))

; (define (pow x y)
;   (if (= 1 x) or (= y 0) 1)
;   (if (even? y) (square (pow x (/ y 2))) (* x (square (pow x (/ (- y 1) 2)))))
; )
(define (pow x y)
  (cond ((or (= y 0) (= 1 x) ) 1)
  (else (if (even? y) (square (pow x (/ y 2))) (* x (square (pow x (/ (- y 1) 2)))) ))
  )
)

