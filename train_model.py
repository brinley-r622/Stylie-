# ============================================================
# Trains:
# 1. Face Shape
# 2. Hair Type
# 3. Skin Tone
#
# Runs automatically without clicking anything.
# Saves best models to Google Drive.
# ============================================================


import os
import tensorflow as tf 

from tensorflow.keras import layers, models 
from tensorflow.keras.preprocessing.image import ImageDataGenerator 

from tensorflow.keras.callbacks import (
    EarlyStopping,
    ReduceLROnPlateau,
    ModelCheckpoint
)



# ============================================================
# SAVE LOCATION
# ============================================================

save_folder = "/content/drive/MyDrive/Stylie"



# ============================================================
# GENERAL TRAINING FUNCTION
# ============================================================

def train_model(
    model_name, 
    train_path,
    validation_path, 
    save_file 
):

    print("\n================================")
    print("STARTING:", model_name)
    print("================================")



    # ----------------------------
    # IMAGE GENERATORS
    # ----------------------------

    train_generator = ImageDataGenerator( 

        rescale=1./255, 

        rotation_range=10,
        zoom_range=0.1, 

        width_shift_range=0.08, 

        height_shift_range=0.08, 

        brightness_range=(0.85,1.15),
        horizontal_flip=True 

    )


    validation_generator = ImageDataGenerator( 

        rescale=1./255

    )



    train_data = train_generator.flow_from_directory(

        train_path, 

        target_size=(224,224), 

        batch_size=32, 

        class_mode="categorical", 

        shuffle=True 
    )


    validation_data = validation_generator.flow_from_directory(

        validation_path, 
        target_size=(224,224), 

        batch_size=32, 
        class_mode="categorical", 
        shuffle=False 

    )



    print("\nClasses:")

    print(train_data.class_indices) 



    number_classes = len( 

        train_data.class_indices

    )


    if number_classes == 0: 

        raise Exception(
            "No classes found. Check folder path."

        )



    # ----------------------------
    # MOBILE NET MODEL
    # ----------------------------


    base_model = tf.keras.applications.MobileNetV2( 

        input_shape=(224,224,3),

        include_top=False,

        weights="imagenet" 

    )


    base_model.trainable = False 



    model = models.Sequential([ 


        layers.Input( 

            shape=(224,224,3)

        ),


        base_model,


        layers.GlobalAveragePooling2D(), 


        layers.Dropout(0.3),


        layers.Dense(
            128,

            activation="relu"

        ),


        layers.Dropout(0.3), 


        layers.Dense( 

            number_classes,

            activation="softmax" 

        )


    ])



    model.compile( 


        optimizer=tf.keras.optimizers.Adam(

            learning_rate=0.001 

        ),


        loss="categorical_crossentropy", 

        metrics=["accuracy"] 

    )



    # ----------------------------
    # CALLBACKS
    # ----------------------------


    early_stop = EarlyStopping( 


        monitor="val_accuracy", 


        patience=5,

        restore_best_weights=True, 


        verbose=1 

    )



    reduce_lr = ReduceLROnPlateau( 


        monitor="val_loss", 


        patience=2, 


        factor=0.2, 


        verbose=1 

    )



    checkpoint = ModelCheckpoint( 


        filepath=os.path.join(

            save_folder,

            save_file

        ),


        monitor="val_accuracy", 


        save_best_only=True, 

        verbose=1 

    )



    # ----------------------------
    # TRAIN 20 EPOCHS
    # ----------------------------


    model.fit( 


        train_data, 


        validation_data=validation_data, 


        epochs=20, 


        callbacks=[

            early_stop,

            reduce_lr, 
            checkpoint 
        ]

    )



    print("\nFINISHED:", model_name) 




# ============================================================
# 1. FACE SHAPE
# ============================================================

train_model(

    "FACE SHAPE",

    "/content/faceshape/FaceShape Dataset/training_set",

    "/content/faceshape/FaceShape Dataset/testing_set",

    "face_shape_model_retrained.keras"

)



# ============================================================
# 2. HAIR TYPE
# ============================================================

train_model(

    "HAIR TYPE",

    "/content/hairtype/data",

    "/content/hairtype/data",

    "hair_type_model_retrained.keras"

)



# ============================================================
# 3. SKIN TONE
# ============================================================

train_model(

    "SKIN TONE",

    "/content/skintone/train",

    "/content/skintone/train",

    "skin_tone_model_retrained.keras"

)



print("\n================================")

print("ALL STYLIE TRAINING COMPLETE")

print("================================")
