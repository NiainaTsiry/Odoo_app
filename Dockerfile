FROM odoo:16.0

# 1. Copier les addons personnalisés
COPY ./custom_addons /mnt/extra-addons

# 2. Copier la configuration Odoo
RUN mkdir -p /etc/odoo
COPY ./server/odoo.conf /etc/odoo/

# 3. Installer les dépendances supplémentaires
RUN if [ -f /mnt/extra-addons/requirements.txt ]; then \
    pip3 install -r /mnt/extra-addons/requirements.txt; \
    fi

# 4. Créer le dossier de logs
RUN mkdir -p /var/log/odoo && \
    chown odoo:odoo /var/log/odoo

# Exposer le port Odoo
EXPOSE 8069

# Commande de démarrage
CMD ["odoo", "--config=/etc/odoo/odoo.conf"]