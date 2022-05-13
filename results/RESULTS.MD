# Results

All results were trained on the Cityscapes dataset.

`train/`:

`train-512x1024_student_batch12-20220507-131130_DISTILLED_100epochs` - training of student model distilled (for 100 epochs) from teacher model (trained for 100 epochs).

`train-512x1024_teacher_batch12-20220506-142555_TRAINED_100epochs` - training of teacher model for 100 epochs

---

`eval/`:

`eval-512x1024_student_batch12-20220508-184651_DISTILLED_EVAL_100epochs` - evaluation of student model distilled (for 100 epochs) from teacher model (trained for 100 epochs).

---

`latency/`:

contains latency results for student and teacher models running on computer hardware configurations (A) and (B).

(A) - Intel(R) Xeon(R) CPU E5-2623 v4 @ 2.60GHz + NVIDIA 1080 Ti

(B) - AMD Ryzen Threadripper PRO 3975WX 32-Cores + NVIDIA 3080 Ti

Further details on the CPU can be found in the `cpu_A.txt` and `cpu_B.txt` files.