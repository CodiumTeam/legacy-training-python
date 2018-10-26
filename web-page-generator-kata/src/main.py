# coding=utf-8
from users_static_webpage_generator import UsersStaticWebPageGenerator
from user import User

users = [
    User("Teresa Rodríguez",
        "El mundo de la edición me atrapó en el momento que realicé mis prácticas en la Editorial Gamma, en 4° de carrera. Estas prácticas me llevaron a cursar el Máster en Edición en la UPF - English School of Management y a hacer prácticas en Ediciones Minotauro (Grupo Planeta). Ahora también me ha atrapado el mundo de la librería, gracias a mi experiencia como librera de refuerzo en FNAC El Prado.\n" +
        "Otra de mis pasiones es el teatro. Actualmente participo con el grupo de teatro DDD3 en La Profecía en Palma de Mallorca."
    ),

    User("Alfonso de Vahía",
        "En este espacio no hablaré ni de logros, ni de aptitudes, sino del por qué terminé trabajando en el mundo editorial en Barcelona.\n\n" +
        "Cursé Magisterio de Educación Infantil, porque creo que la infancia es una etapa fundamental para el correcto desarrollo del individuo. Los valores son importantísimos en nuestra sociedad: son los que nos definen como especie y, sin ellos, cualquier tipo de avance social se vería ridículo y descompensado. Por eso decidí conocer de qué manera el individuo nace y se hace. La educación me ha ofrecido la magnífica necesidad de observar el mundo, escucharlo y trabajar para una mejora del mismo. Porque ser maestro no se ciñe en impartir una clase, va mucho más allá: haces de psicólogo, de productor audiovisual, de padre, de compañero, de asesor, de actor..."
    ),

    User("Geraldine Rivia", "Redactora, editora y correctora con base en Madrid.\n\n" +
        "Corrección profesional ortotipográfica de diferentes tipos de textos (libros de texto, artículos de revistas, casos económicos, etc.) y corrección de estilo. \n\n" +
        "Especialidades: creación de contenidos, adaptación de los contenidos a los canales sociales, redacción creativa, edición de textos, corrección ortotipográfica profesional, branded content, periodismo digital, social media, community manager, dinamización de comunidades online."
    )
]

generator = UsersStaticWebPageGenerator()
generator.generateFile(users)
