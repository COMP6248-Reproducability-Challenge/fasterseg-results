# Results

All results were trained on the Cityscapes dataset.

---

`test/`:

contains test results submitted to Cityscapes and csv files containing the returned evaluations

`merged.csv` contains all the test results in a single file.

---

`train/`:

`100epoch_distilled_student_from_100epoch_teacher/` - distillation of student model (for 100 epochs) from teacher model (trained for 100 epochs).

`100epoch_trainscratch_teacher/` - training of teacher model for 100 epochs

`100epoch_trainscratch_student/` - training of student model for 100 epochs

`300epoch_trainscratch_student/` - training of student model for 300 epochs

`100epoch_distilled_student_from_pretrain_teacher/` - distillation of student model (for 100 epochs) from pre-trained teacher model


---

`eval/`:

`eval-512x1024_student_batch12-20220508-184651_DISTILLED_EVAL_100epochs` - evaluation of student model distilled (for 100 epochs) from teacher model (trained for 100 epochs).

---

`latency/`:

contains latency results for student and teacher models running on computer hardware configurations (A) and (B).

(A) - Intel(R) Xeon(R) CPU E5-2623 v4 @ 2.60GHz + NVIDIA 1080 Ti

(B) - AMD Ryzen Threadripper PRO 3975WX 32-Cores + NVIDIA 3080 Ti

Further details on the CPU can be found in the `cpu_A.txt` and `cpu_B.txt` files.