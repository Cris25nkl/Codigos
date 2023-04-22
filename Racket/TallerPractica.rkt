#lang eopl

(define list-set
  (lambda (lista n x)
    (cond
      [(null? lista) '()]
      [(= n 0) (append (cdr lista) (list x))]
      [else (append (list (car lista))
                    (list-set (cdr lista) (- n 1) x))]
      )
    )
  )

(define list-tails
  (lambda (lista)
    (cond
      [(null? lista) '()]
      [else (append (list lista)
                    (list-tails (cdr lista)))]
      )
    )
  )
(define exist?
  (lambda (pred lista)
    (cond
      [(null? lista) #F]
      [(pred (car lista)) #T]
      [else (exist? pred (cdr lista))])))



(define list-facts
  (lambda (n)
    (cond
      [(= n 1) '(1)]
      [else
       (append
        
        (list (* n (car(list-facts (- n 1)))))
        (list-facts (- n 1)))]
      )
    )
  )

(define lista-fibunacci
  (lambda (n)
    (cond
      [(< n 0) '()]
      [(= n 0) '(0)]
      [else (append '(0 1))]
      
      ))) 