#lang racket
(define a 4)
(define b "hola")

(define funcion
  (lambda (x y) (+ x y)))


(define edad_D
  (lambda (edad)
    (cond
      [(and (>= edad 0)(< edad 18))"No entra"]
      [(and (>= edad 18) (<= edad 30))"Seccion jovenes"]
      [(and (> edad 30)(< edad 50))"Seccion adultos"]
      [(>= edad 50)"Viejoteca"]
      [else "Edad no valida"]
      )
    )
  )

;listas
(cons 1 (cons 2 (cons 3 empty)))
(list 1 2 3)
'(1 2 3)
(define l1 '(1 2 (a b) (1 2 3)))


(define l2 '(1 2 3 4 5 6 7 8 9))

(define sumalista
  (lambda (lst)
    (cond
      [(null? lst) 0]
      [else
       (+ (car lst) (sumalista (cdr lst)))
       ]
      )
    )
  )


