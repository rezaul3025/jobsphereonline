module.controller('jobsphereonlineController', ['$http', '$scope', '$window', function($http, $scope, $window) {
	
 $scope.searchTag = function(searchKey){

 	return $http.get('/searchtags', {
      params: {
        searchKey: searchKey
      }
    }).then(function(response){
    	var tags = [];
    	if(response.data != null && typeof response.data != 'undefined'){
    		for(i in response.data){
    			tags.push(response.data[i].fields.name);
    		}
    	}
      return tags;
    });
}

$scope.searchLocations = function(searchKey){

 	return $http.get('/searchlocations', {
      params: {
        searchKey: searchKey
      }
    }).then(function(response){
    	var locations = [];
    	if(response.data != null && typeof response.data != 'undefined'){
    		for(i in response.data){
    			locations.push(response.data[i].fields.name);
    		}
    	}
      return locations;
    });
}

$scope.postJob=function(job){

	$http({
            method : "POST",
            url : "/postjob/",
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded'
            },
            data:$.param({
            	'title' : job.title,
                'description':job.description,
                'applicationoption':job.applicationoption,
                'applicationurl':job.applicationurl,
                'category':job.category,
                'location':job.location,
                'tag':job.tag
               })
            }).then(function mySucces(response) {
                  //alert(response.data);
                  window.location='/job/jobpostsuccess/'
            }, function myError(response) {
                  //alert(response.data);
     });
}

}]);