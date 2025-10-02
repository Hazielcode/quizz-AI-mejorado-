from quizzes.models import Quiz, Question, Choice

# 🔄 Limpia todo antes
Choice.objects.all().delete()
Question.objects.all().delete()
Quiz.objects.all().delete()

def add_question(quiz, text, correct, wrongs):
    q = Question.objects.create(quiz=quiz, text=text)
    Choice.objects.create(question=q, text=correct, is_correct=True)
    for w in wrongs:
        Choice.objects.create(question=q, text=w, is_correct=False)

# ============================
# QUIZ 1: Python Básico
# ============================
quiz1 = Quiz.objects.create(
    title="Python Básico",
    description="Preguntas introductorias de Python",
    image="https://raw.githubusercontent.com/abranhe/programming-languages-logos/master/src/python/python.svg"
)

add_question(quiz1, "¿Qué es Python?", "Un lenguaje de programación", ["Un reptil", "Un sistema operativo"])
add_question(quiz1, "¿Qué extensión usan archivos Python?", ".py", [".java", ".js"])
add_question(quiz1, "¿Cómo se imprime algo en Python?", "print()", ["echo()", "console.log()"])
add_question(quiz1, "¿Qué estructura se usa para iterar?", "for", ["switch", "if"])
add_question(quiz1, "¿Qué imprime 2 + 2?", "4", ["22", "Error"])

# ============================
# QUIZ 2: JavaScript Fundamentals
# ============================
quiz2 = Quiz.objects.create(
    title="JavaScript Fundamentals",
    description="Conceptos clave de JavaScript",
    image="https://raw.githubusercontent.com/abranhe/programming-languages-logos/master/src/javascript/javascript.svg"
)

add_question(quiz2, "¿Qué significa JS?", "JavaScript", ["Java Source", "Just Syntax"])
add_question(quiz2, "¿Qué símbolo es para comentarios?", "//", ["#", "/* */"])
add_question(quiz2, "¿Qué palabra declara variables?", "let", ["varr", "def"])
add_question(quiz2, "¿Qué operador suma valores?", "+", ["-", "*"])
add_question(quiz2, "¿Qué imprime console.log(3+2)?", "5", ["32", "Error"])

# ============================
# QUIZ 3: Bases de Datos
# ============================
quiz3 = Quiz.objects.create(
    title="Bases de Datos",
    description="SQL y conceptos básicos",
    image="https://cdn-icons-png.flaticon.com/512/2772/2772128.png"
)

add_question(quiz3, "¿Qué es SQL?", "Structured Query Language", ["Simple Quick Language", "Script Query Logic"])
add_question(quiz3, "¿Qué comando selecciona datos?", "SELECT", ["INSERT", "UPDATE"])
add_question(quiz3, "¿Qué comando elimina datos?", "DELETE", ["REMOVE", "DROP"])
add_question(quiz3, "¿Qué comando crea tabla?", "CREATE TABLE", ["NEW TABLE", "ADD TABLE"])
add_question(quiz3, "¿Qué tipo es este DB?", "Relacional", ["NoSQL", "Distribuida"])

# ============================
# QUIZ 4: Redes
# ============================
quiz4 = Quiz.objects.create(
    title="Redes",
    description="Conceptos básicos de redes de computadoras",
    image="https://cdn-icons-png.flaticon.com/512/3064/3064197.png"
)

add_question(quiz4, "¿Qué significa IP?", "Internet Protocol", ["Internal Port", "Interconnected Path"])
add_question(quiz4, "¿Qué protocolo es web?", "HTTP/HTTPS", ["FTP", "SMTP"])
add_question(quiz4, "¿Qué es LAN?", "Local Area Network", ["Large Area Network", "Logical Access Node"])
add_question(quiz4, "¿Qué dispositivo conecta redes diferentes?", "Router", ["Switch", "Hub"])
add_question(quiz4, "¿Qué puerto usa HTTP por defecto?", "80", ["21", "25"])

# ============================
# QUIZ 5: IoT
# ============================
quiz5 = Quiz.objects.create(
    title="Internet of Things",
    description="Fundamentos de IoT",
    image="https://cdn-icons-png.flaticon.com/512/2721/2721297.png"
)

add_question(quiz5, "¿Qué significa IoT?", "Internet of Things", ["Internal of Tech", "Input of Tools"])
add_question(quiz5, "¿Qué placa es común en IoT?", "ESP32", ["GTX 1080", "Pentium 4"])
add_question(quiz5, "¿Qué protocolo usan sensores IoT?", "MQTT", ["SMTP", "POP3"])
add_question(quiz5, "¿Qué mide el sensor DHT11?", "Temperatura y Humedad", ["Voltaje", "pH"])
add_question(quiz5, "¿Qué es Arduino?", "Plataforma de prototipado", ["Lenguaje", "SO"])

# ============================
# QUIZ 6: Linux
# ============================
quiz6 = Quiz.objects.create(
    title="Linux",
    description="Sistema operativo y comandos básicos",
    image="https://cdn-icons-png.flaticon.com/512/518/518713.png"
)

add_question(quiz6, "¿Qué comando lista archivos?", "ls", ["rm", "cd"])
add_question(quiz6, "¿Qué crea directorio?", "mkdir", ["makedir", "createdir"])
add_question(quiz6, "¿Qué borra archivo?", "rm", ["delete", "erase"])
add_question(quiz6, "¿Archivo que guarda usuarios?", "/etc/passwd", ["/etc/user", "users.txt"])
add_question(quiz6, "¿Directorio actual se muestra con?", "pwd", ["cd", "dir"])

# ============================
# QUIZ 7: Ciberseguridad
# ============================
quiz7 = Quiz.objects.create(
    title="Ciberseguridad",
    description="Fundamentos de seguridad informática",
    image="https://cdn-icons-png.flaticon.com/512/3135/3135715.png"
)

add_question(quiz7, "¿Qué significa CIA en seguridad?", "Confidencialidad, Integridad, Disponibilidad", ["Cyber Internet Attack", "Control Info Access"])
add_question(quiz7, "¿Qué es un firewall?", "Sistema que filtra tráfico", ["Un virus", "Un OS"])
add_question(quiz7, "¿Qué es phishing?", "Engaño para robar datos", ["Tipo de firewall", "Un antivirus"])
add_question(quiz7, "¿Qué reemplaza HTTP seguro?", "HTTPS", ["FTP", "SMTP"])
add_question(quiz7, "¿Qué significa VPN?", "Virtual Private Network", ["Verified Protocol Network", "Virtual Public Node"])

# ============================
# QUIZ 8: Inteligencia Artificial
# ============================
quiz8 = Quiz.objects.create(
    title="Inteligencia Artificial",
    description="Conceptos básicos de IA",
    image="https://cdn-icons-png.flaticon.com/512/4712/4712109.png"
)

add_question(quiz8, "¿Qué significa IA?", "Inteligencia Artificial", ["Intranet Adv", "Interfaz Avanzada"])
add_question(quiz8, "¿Qué lenguaje es popular en IA?", "Python", ["C", "Pascal"])
add_question(quiz8, "¿Qué es Machine Learning?", "Aprendizaje automático", ["Programación manual", "Compilación"])
add_question(quiz8, "¿Qué es un modelo entrenado?", "Algoritmo con datos aprendidos", ["Un servidor", "Un lenguaje"])
add_question(quiz8, "¿Qué librería se usa en IA?", "TensorFlow", ["Bootstrap", "Spring"])

print("✅ Datos con imágenes insertados con éxito!")
