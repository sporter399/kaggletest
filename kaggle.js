var api = {
    root: "https://api.kaggle.com",
    token: "920d2ddd826ff7dbdfa508cf8a168f71" 
  }
  console.log("line 5"); 
  var viewAPI = new Vue({
      el: '#mount-target',
      data: function() {
          return {
             
            APIdata: [],
          };
      },
    
      
      methods: {
          testAPI: function () {
              
              fetch(`${api.root}/configuration?api_key=${api.token}`)
                      .then(resp => resp.ok ? resp.json() : Promise.reject(resp))
                      .then((response) => {
                          console.log("We got a response from Kaggle!");
                          
                          this.APIdata = response.results;
  
                      });
          },
          
          
      },
     
  });
  