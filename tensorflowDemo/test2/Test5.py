# coding:utf-8
import tensorflow as tf
import numpy as np

# 定义一个特征数组，这里仅提供实数特征
def model(features, labels, mode):
  # 构建线性模型和预设值
  W = tf.get_variable("W", [1], dtype=tf.float64)
  b = tf.get_variable("b", [1], dtype=tf.float64)
  y = W*features['x'] + b
  # 损益子图
  loss = tf.reduce_sum(tf.square(y - labels))
  # 训练子图
  global_step = tf.train.get_global_step()
  optimizer = tf.train.GradientDescentOptimizer(0.01)
  train = tf.group(optimizer.minimize(loss),
                   tf.assign_add(global_step, 1))
  # ModelFnOps方法将创建我们自定义的一个抽象模型。
  return tf.contrib.learn.ModelFnOps(
      mode=mode, predictions=y,
      loss=loss,
      train_op=train)

if __name__ == '__main__':
    estimator = tf.contrib.learn.Estimator(model_fn=model)
    x = np.array([1., 2., 3., 4.])
    y = np.array([0., -1., -2., -3.])
    input_fn = tf.contrib.learn.io.numpy_input_fn({"x": x}, y, 4, num_epochs=1000)

    # 训练数据
    estimator.fit(input_fn=input_fn, steps=1000)
    # 评估模型
    print(estimator.evaluate(input_fn=input_fn, steps=10))












