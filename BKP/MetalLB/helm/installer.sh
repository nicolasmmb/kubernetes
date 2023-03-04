#Switch to home directory
cd
#Create a directory for helm
mkdir helm
#Switch to helm directory
cd helm
#Download helm installer
curl -fsSL -o get_helm.sh https://raw.githubusercontent.com/helm/helm/main/scripts/get-helm-3
#change permissions to execute
chmod 700 get_helm.sh
#install helm
./get_helm.sh

#check if helm is installed
helm version

