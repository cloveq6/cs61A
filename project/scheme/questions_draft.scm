; (define (caar x) (car (car x)))
; (define (cadr x) (car (cdr x)))
; (define (cdar x) (cdr (car x)))
; (define (cddr x) (cdr (cdr x)))

; ; Some utility functions that you may find useful to implement

; ; (define (zip pairs)
; ;   'replace-this-line)


; ;; Problem 15
; ;; Returns a list of two-element lists
; (define (enumerate s)
;   ; BEGIN PROBLEM 15
;   (define (enumerate-from n remainder-s) (
;     (if (null? remainder-s) nil 
;     (cons '(n (car remainder-s)) (enumerate-from (+ n 1) (cdr remainder-s)))
;     )
;   )
;   )
;   (enumerate-from 0 s)
; )
;   ; END PROBLEM 15
