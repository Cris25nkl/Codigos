#lang racket

(define l1 '())
(define l2 3)
(define l3 'x)
(define l4 '(x (y 3 s) (y y 4)))

;1a
(define EnLista?
  (lambda (l)
    (cond
      [(null? l) #t]
      [(symbol? l) #t]
      [(number? l) #t]
      [else
       (and
        [symbol? (car l)]
        [EnLista? (cadr l)]
        [EnLista? (caddr l)])])))

;1b
(define buscar-simbolo
  (lambda (l s)
    (cond
      [(null? l) #f]
      [(number? l) (eqv? l s)]
      [(symbol? l) (eqv? l s)]
      [else
       (or
        [eqv? (car l) s]
        [buscar-simbolo (cadr l) s]
        [buscar-simbolo (caddr l) s])])))  
