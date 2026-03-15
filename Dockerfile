# Image de base Ubuntu 22.04
FROM ubuntu:22.04

# Éviter les interactions pendant l'installation
ENV DEBIAN_FRONTEND=noninteractive
ENV WEBOTS_HOME=/usr/local/webots

# Installer les dépendances système
RUN apt-get update && apt-get install -y \
    wget \
    python3 \
    python3-pip \
    xvfb \
    libgl1 \
    libegl1 \
    libxkbcommon0 \
    libdbus-1-3 \
    libxcb-icccm4 \
    libxcb-image0 \
    libxcb-keysyms1 \
    libxcb-randr0 \
    libxcb-render-util0 \
    libxcb-xinerama0 \
    gnupg \
    software-properties-common \
    && rm -rf /var/lib/apt/lists/*

# Installer Webots
RUN wget -qO- https://cyberbotics.com/Cyberbotics.asc | apt-key add - && \
    apt-add-repository 'deb https://cyberbotics.com/debian/ binary-amd64/' && \
    apt-get update && \
    apt-get install -y webots && \
    rm -rf /var/lib/apt/lists/*

# Installer les dépendances Python
RUN pip3 install pytest pytest-html numpy

# Copier le projet
COPY . /app
WORKDIR /app

# Créer le dossier reports
RUN mkdir -p reports

# Variables d'environnement Webots
ENV PYTHONPATH=$WEBOTS_HOME/lib/controller/python
ENV LD_LIBRARY_PATH=$WEBOTS_HOME/lib/controller
ENV DISPLAY=:99

# Script de lancement
CMD ["bash", "-c", "\
    export DISPLAY=:99 && \
    Xvfb :99 -screen 0 1024x768x24 & \
    sleep 3 && \
    echo ' Lancement Webots...' && \
    timeout 150 webots --mode=fast --batch simulation/pick_and_place.wbt & \
    WEBOTS_PID=$! && \
    echo ' Attente du JSON...' && \
    for i in $(seq 1 60); do \
        if [ -f /app/reports/simulation_results.json ]; then \
            echo ' JSON trouvé !'; \
            break; \
        fi; \
        sleep 3; \
    done && \
    kill $WEBOTS_PID 2>/dev/null || true && \
    sleep 2 && \
    echo ' Lancement pytest...' && \
    pytest tests/ -v --html=reports/report.html || true \
"]