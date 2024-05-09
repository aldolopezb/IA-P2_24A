#Aldo López Barrios
#21310106
#--------------------------
import rospy  # Importamos la biblioteca ROS para Python

# Definimos una función de callback que se llamará cada vez que recibamos un mensaje en el topic '/robot_position'
def callback(data):
    rospy.loginfo("Posición actual del robot: %s", data.data)  # Imprimimos la posición recibida

def listener():
    rospy.init_node('robot_listener', anonymous=True)  # Inicializamos el nodo ROS llamado 'robot_listener'

    # Nos suscribimos al topic '/robot_position' y especificamos la función de callback
    rospy.Subscriber("/robot_position", String, callback)

    rospy.spin()  # Mantenemos el programa en funcionamiento hasta que se cierre

if __name__ == '__main__':
    try:
        listener()  # Llamamos a la función listener() para iniciar la escucha de mensajes
    except rospy.ROSInterruptException:
        pass
