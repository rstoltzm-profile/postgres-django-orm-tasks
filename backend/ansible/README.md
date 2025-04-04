# Ansible setup
## wsl2 ubuntu
```
sudo apt update
sudo apt install ansible -y
ansible --version
ansible-galaxy collection install community.postgresql
```

## Run playbook
* note: bare minimum setup to get running, can be greatly improved as needed
```
ansible-playbook -i inventory deploy_postgres.yml
```
