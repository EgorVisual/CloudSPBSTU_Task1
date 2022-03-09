curl 'http://192.168.17.10:5000/helloserverget'
curl 'http://192.168.17.10:5000/helloservergetlist/Egor'
curl -d "name=Egor&height=190" -X PUT 'http://192.168.17.10:5000/helloserverput'
curl -d "name=Vova&height=165" -X POST 'http://192.168.17.10:5000/helloserverpost'