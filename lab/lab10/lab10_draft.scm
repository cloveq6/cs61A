(define (abs x)
  (if (< x 0)
      (- x)
      x))

(define (fun x)
    (define (square y) (* y y))
    (define (cube z) (* z z z))
    (+ (square x) (cube x))
)


(define (repeat k fn mes)
  ; Repeat fn k times.
  (fn mes)
  (if (> k 1) (repeat (- k 1) fn mes)))

(define (silly mes) (if (> 10 1) (print mes))) 

(define (xx a)
(if (> a 1) (repeat 2 fun a))
)

(define (xxx b mes) 
(if (> b 1) (repeat b silly mes))
)


(define (length items)
  (if (null? items)
      0
      (+ 1 (length (cdr items)))))


(define c (let ((a 3) 
 (b (+ 2 2))) 
 (sqrt (+ (* a a) (* b b)))))


 (define cc (let ((a -1)) (abs a)))


 (define (ppp lst)
 (if (null? lst) (print 'finish)  (begin (print (car lst)) (ppp (cdr lst))))
 )


  (define (p_new item lst)
 (if (null? lst) (print 'finish)  
 (begin (if (=(car lst) item) () (print (car lst))) (p_new item (cdr lst)))
 )
 )


   (define (p_new_plus item lst)
 (if (null? lst) nil  
 (if (=(car lst) item) (p_new_plus item (cdr lst)) (begin (print (car lst)) (p_new_plus item (cdr lst))))
 )
 )


   (define (p_final item lst)
 (if (null? lst) nil  
 (if (=(car lst) item) (p_final item (cdr lst)) (append (list (car lst)) (p_final item (cdr lst))))
 )
 )

