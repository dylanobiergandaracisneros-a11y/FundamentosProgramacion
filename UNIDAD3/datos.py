###Almacenar las listas compartidas del sistema.###

alumnos = [
          {"num_control":"26040200", "nombre":"Superman",  "carrera":"Ingeniería en Inteligencia Artificial"},
          {"num_control":"26040201", "nombre":"Bat Man",   "carrera":"Ingeniería en Sistemas de Computacion"},
          {"num_control":"26040202", "nombre":"Spiderman", "carrera":"Ingeniería en Sistemas de Computacion"},
          {"num_control":"26040203", "nombre":"Catwoman",  "carrera":"Biomedico"},
          {"num_control":"26040204", "nombre":"Iron Man",  "carrera":"Ingeniería en Inteligencia Artificial"},
          {"num_control":"26040205", "nombre":"Daredevil", "carrera":"Arquitectura"}
          ]

nuevo_prestamo = [
                 { "num_control":"26040200", "programas":"Python, Java, VS Code", "aula":"LC1", "id" "PC-LC1-02" "fecha_y_hora":"9/10/2026 07:30:00" },
                 { "num_control":"26040201", "programas":"AutoCAD, MATLAB",       "aula":"LC1", "id" "PC-LC1-03" "fecha_y_hora":"9/10/2026 07:30:00" },
                 { "num_control":"26040202", "programas":"Python, Java, VS Code", "aula":"LC2", "id" "PC-LC2-02" "fecha_y_hora":"9/10/2026 07:30:00" },
                 { "num_control":"26040203", "programas":"AutoCAD, MATLAB",       "aula":"LC2", "id" "PC-LC2-03" "fecha_y_hora":"9/10/2026 07:30:00" },
                 { "num_control":"26040204", "programas":"Python, Java, VS Code", "aula":"LC3", "id" "PC-LC3-02" "fecha_y_hora":"9/10/2026 07:30:00" },
                 { "num_control":"26040205", "programas":"AutoCAD, MATLAB",       "aula":"LC3", "id" "PC-LC2-03" "fecha_y_hora":"9/10/2026 07:30:00" }
                 ]
historial_necesidades = [
    { "programa" "Photoshop", "fecha_y_hora" "9/10/2026 07:30:00"},
    { "programa" "photoshop", "fecha_y_hora" "12-10-2026 17:05:59"}
]

# Cada valor en la lista de computadoras tiene su lista correspondiente con el
# aula donde esta ubicada, el software instalado y el estado de esa computadora
computadoras = [
                { "id":"PC-LC1-01", "aula":"LC1", "programas":"Python, VS Code",       "estado":"Disponible"},
                { "id":"PC-LC1-02", "aula":"LC1", "programas":"Python, Java, VS Code", "estado":"Prestada"},
                { "id":"PC-LC1-03", "aula":"LC1", "programas":"AutoCAD, MATLAB",       "estado":"Reservada"},
                { "id":"PC-LC2-01", "aula":"LC2", "programas":"Python, VS Code",       "estado":"Disponible"},
                { "id":"PC-LC2-02", "aula":"LC2", "programas":"Python, Java, VS Code", "estado":"Prestada"},
                { "id":"PC-LC2-03", "aula":"LC2", "programas":"AutoCAD, MATLAB",       "estado":"Reservada"},
                { "id":"PC-LC3-01", "aula":"LC3", "programas":"Python, VS Code",       "estado":"Disponible"},
                { "id":"PC-LC3-02", "aula":"LC3", "programas":"Python, Java, VS Code", "estado":"Prestada"},
                { "id":"PC-LC3-03", "aula":"LC3", "programas":"AutoCAD, MATLAB",       "estado":"Reservada"},
                { "id":"PC-LC3-04", "aula":"LC3", "programas":"Python, VS Code",       "estado":"Mantenimiento"},
                ]