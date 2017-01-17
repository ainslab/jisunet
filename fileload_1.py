import tensorflow as tf
import os
from PIL import Image
# Can replace to matplotlib
#
#
# def search(dirname):
#     try:
#         filenames = os.listdir(dirname)
#         for filename in filenames:
#             full_filename = os.path.join(dirname, filename)
#             if os.path.isdir(full_filename):
#                 search(full_filename)
#             else:
#                 ext = os.path.splitext(full_filename)[-1]
#                 if ext == '.jpg':
#                     return(full_filename)
#     except PermissionError:
#         pass
#
batch_size = 10

def image_batch(directory_name, batch_size):
    try:
        image_list = []
        filenames = os.listdir(directory_name)
        for i in range(batch_size):
            for filename in filenames:
                full_filename = os.path.join(directory_name, filename)
                if os.path.isdir(full_filename):
                    image_batch(full_filename, batch_size)
                else:
                    ext = os.path.splitext(full_filename)[-1]
                    if ext == '.jpg':
                        if full_filename == image_list:
                            continue
                        else:
                            image_list.append(full_filename)

        return(image_list)
    except PermissionError:
        pass

image_dir = image_batch("C:/Users\Park\PycharmProjects\Practice", batch_size)
image_set = list(set(image_dir))
# print(image_set)
for image_set in image_set:
    filename_list = [image_set]
    reader = tf.WholeFileReader()
    filename_queue = tf.train.string_input_producer(filename_list)
    key, contents = reader.read(filename_queue)

    img = tf.image.decode_jpeg(contents)

    with tf.Session() as sess:
        coord = tf.train.Coordinator()
        threads = tf.train.start_queue_runners(coord=coord)

        image = sess.run(img)
        Image.fromarray(image).show()
        print(image)
        coord.request_stop()
        coord.join(threads)





# height = 1200
# width = 900
#
# image_byte = width * height
#
# reader = tf.WholeFileReader(record_bytes=image_byte)
#
# filename_queue = tf.train.string_input_producer(['./Jisoo.jpg'])
# key, contents = reader.read(filename_queue)
# img = tf.image.decode_jpeg(contents)
#
#
# with tf.Session() as sess:
#     coord = tf.train.Coordinator()
#     threads = tf.train.start_queue_runners(coord=coord)
#
#     image = sess.run(img)
#     coord.request_stop()
#     coord.join(threads)

