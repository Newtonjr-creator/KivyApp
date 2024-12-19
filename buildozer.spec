[app]
# (str) Title of your application
title = flappybird 

# (str) Package name
package.name = flappybird

# (str) Package domain (e.g., org.test.myapp)
package.domain = com.abhishek.com

# (str) Source code where the main.py is located
source.dir = .

# (str) Main script file
source.main = main.py

# (str) Application version
version = 1.0.0

# (str) Supported orientation (one of: portrait, landscape, sensor)
orientation = portrait

# (list) Permissions required by the application
permissions = INTERNET, READ_EXTERNAL_STORAGE, WRITE_EXTERNAL_STORAGE

# (int) Target Android API (should match installed SDK version)
android.api = 33

# (int) Minimum API (supports Android 4.2 and newer)
android.minapi = 21

# (str) Android SDK directory path
# You can adjust this path if needed
android.sdk_path = /storage/emulated/0/Android/sdk

# (str) Directory for build artifacts
# Default: bin/
android.builddir = ./build

# (list) Add any libraries that your app needs
# Example: requirements = python3, kivy
requirements = python3, pygame

# (list) Local Java .jars to add to the project classpath
# Example: android.add_jars = mylibrary.jar
#android.add_jars = 

# (list) Screenshots
# Example: screenshots = 1.png, 2.jpg
#screenshots =

# (list) Presplash and Icon
# Example: icon.filename = %(source.dir)s/assets/icon.png
# Example: presplash.filename = %(source.dir)s/assets/presplash.png
#icon.filename = ./gallery/sprites/icon.png
presplash.filename = /storage/emulated/0/flappybird/gallery/sprites/message.png

# (bool) Indicate whether the application is fullscreen
fullscreen = 1

# (list) Add Android-specific metadata
# Example: android.meta_data = key=value
#android.meta_data = 

# (list) Custom Java classes
# Example: android.add_src = custom.java
#android.add_src = 

# (str) Extra manifest entries to append at the <manifest> tag
# android.manifest_intent_filters = <data android:scheme="example" />
#android.manifest_intent_filters = 

# (list) Custom libraries to include
# android.add_libraries = 

[buildozer]
# (str) Log level (one of: 1=ERROR, 2=WARNING, 3=INFO, 4=DEBUG, 5=TRACE)
log_level = 2

# (int) Number of concurrent build jobs
# Default: 1
# 0 means use all available CPUs.
jobs = 1
