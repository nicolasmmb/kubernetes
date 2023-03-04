# docker build -t main-tests-deploy . --platform linux/amd64,linux/arm64,linux/arm/v7                        
# Error response from daemon: "amd64,linux" is an invalid component of "linux/amd64,linux/arm64,linux/arm/v7": platform specifier component must match "^[A-Za-z0-9_-]+$": invalid argument

# docker build -t nicolasmmb/main-tests-deploy:latest 
# docker tag main-tests-deploy nicolasmmb/main-tests-deploy:latest
# docker push nicolasmmb/main-tests-deploy:latest

# WORKs
# docker buildx create --use --name multi-arch-deploy 
docker buildx build --platform linux/amd64,linux/arm64,linux/arm/v7 -t nicolasmmb/main-tests-deploy:latest --push .