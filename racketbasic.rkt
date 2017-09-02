;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-beginner-reader.ss" "lang")((modname racketbasic) (read-case-sensitive #t) (teachpacks ((lib "dir.rkt" "teachpack" "htdp"))) (htdp-settings #(#t constructor repeating-decimal #f #t none #f ((lib "dir.rkt" "teachpack" "htdp")) #f)))
;;#lang racket

;;(provide (all-defined-out))

(define x 3)
(define y (+ x 2))

(define cube1
  (lambda (x)
         (* x (* x x))))
(define (cube3 x)
  (* x x x))

(define (pow1 x y)
  (if (= y 0)
      1
      (* x (pow1 x ( - y 1)))))