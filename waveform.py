import numpy as np
import matplotlib.pyplot as plt
from sympy.logic.boolalg import Or, And, Not
from sympy.abc import A, B, C, D
from sympy import lambdify

# Thiết lập biểu thức logic
expression = Or(And(Not(A), Not(B), C, Not(D)), And(Not(A), Not(B), Not(C)), A)

# Chuyển đổi biểu thức thành hàm có thể tính toán giá trị với numpy
logic_function = lambdify((A, B, C, D), expression, 'numpy')

# Thiết lập các tín hiệu đầu vào (các mẫu tuần hoàn)
time_steps = 16  # 2^4 = 16 tổ hợp có thể có cho 4 biến
time = np.arange(time_steps)

# Tạo các giá trị đầu vào theo dạng sóng (tuần hoàn 0-1)
A_signal = np.array([((time_step) & 1) ^ 1 for time_step in time])  # Bắt đầu từ 1 và mỗi 2 timestep mới biến đổi
B_signal = np.array([(time_step >> 1) & 1 ^ 1 for time_step in time])
C_signal = np.array([(time_step >> 2) & 1 ^ 1 for time_step in time])  # Mỗi 4 timestep mới biến đổi
D_signal = np.array([(time_step >> 3) & 1 ^ 1 for time_step in time])

# Tính toán đầu ra X dựa trên các tín hiệu đầu vào
X_signal = logic_function(A_signal, B_signal, C_signal, D_signal)

# Vẽ dạng sóng
plt.figure(figsize=(10, 6))

# Hàm tiện ích để vẽ từng tín hiệu
def plot_waveform(signal, label, position):
    plt.plot(time, signal + position, label=label, drawstyle='steps-post')
    plt.fill_between(time, position, signal + position, step="post", alpha=0.3)

# Vẽ các tín hiệu đầu vào
plot_waveform(A_signal, 'A', 4)
plot_waveform(B_signal, 'B', 3)
plot_waveform(C_signal, 'C', 2)
plot_waveform(D_signal, 'D', 1)

# Vẽ tín hiệu đầu ra
plot_waveform(X_signal, 'X', 0)

# Cài đặt trục hoành và trục tung
plt.xticks(time)  # Hiển thị tất cả các giá trị từ 0 đến 15 trên trục hoành
plt.yticks([4, 3, 2, 1, 0], ['A', 'B', 'C', 'D', 'X'])  # Đặt nhãn trục tung

plt.xlabel('Time')
plt.ylabel('Signals')
plt.legend(loc='upper right')
plt.title('Logic Waveform for A, B, C, D and Output X')
plt.grid(True)
plt.show()
