--- voaP2PPlot.py	2017-05-05 07:50:17.000000000 -0500
+++ src/pythonprop/voaP2PPlot.py	2017-05-05 07:50:40.000000000 -0500
@@ -212,7 +212,7 @@
             else :
                 y_max = math.ceil(plot_max_freq / 5.0) * 5.0
             #resize the image
-            image_buffer = image_buffer[0:y_max-1,:]
+            image_buffer = image_buffer[0:int(y_max)-1,:]
 
             y_ticks = [2, 5]
             for y_tick_value in np.arange(10, y_max+1, 5):
