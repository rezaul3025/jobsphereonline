//var module = angular.module('healthcareWebApp', ['ui.bootstrap']);

module.directive('jsoTagDiv', function () {
    return {
        restrict: 'E',
        replace: true,
        template: function (element, attrs) {
        
            //var form = cg.getPropertyOrDefault(attrs, "cgForm", "ciForm");
           // var field = cg.getPropertyOrDefault(attrs, "cgField", hpo);
            //var errors = cg.getPropertyOrDefault(attrs, "cgErrorMessages", "clinicalInfoHpoMessages");
            //return cgDirectives.inputTemplateSelect(form, field, errors, errors, "cg-hpo=''", "Select hpo terms", element);
        	return '<input type="text" style="width:555px" name="'+attrs.name+'" jso-tag="" id="'+attrs.id+'" ></input>';
        	
        }
    	
    }
});

module.directive('jsoTag',['hcService','$http', function (hcService, $http) {
	return {
        restrict: 'EA',
        require: 'ngModel',
        link: function (scope, element, attrs, ngModel) {
           
            var selectParams = hcService.getRemoteMultiPagedConfig1(element, ngModel, 'Select tags', true, "/gettags", 5, {});
                     
            hcService.generateSelect2Box1(element, selectParams, scope, ngModel, attrs.ngModel);
           
        }
    };
}]);

module.directive('jsoLocationDiv', function () {
    return {
        restrict: 'E',
        replace: true,
        template: function (element, attrs) {
        
            //var form = cg.getPropertyOrDefault(attrs, "cgForm", "ciForm");
           // var field = cg.getPropertyOrDefault(attrs, "cgField", hpo);
            //var errors = cg.getPropertyOrDefault(attrs, "cgErrorMessages", "clinicalInfoHpoMessages");
            //return cgDirectives.inputTemplateSelect(form, field, errors, errors, "cg-hpo=''", "Select hpo terms", element);
          return '<input type="text" style="width:380px" name="'+attrs.name+'" jso-location="" id="'+attrs.id+'" ></input>';
          
        }
      
    }
});

module.directive('jsoLocation',['hcService','$http', function (hcService, $http) {
  return {
        restrict: 'EA',
        require: 'ngModel',
        link: function (scope, element, attrs, ngModel) {
           
            var selectParams = hcService.getRemoteMultiPagedConfig1(element, ngModel, 'Select locations', true, "/getlocations", 5, {});
                     
            hcService.generateSelect2Box1(element, selectParams, scope, ngModel, attrs.ngModel);
           
        }
    };
}]);

module.directive('jsoCategoryDiv', function () {
    return {
        restrict: 'E',
        replace: true,
        template: function (element, attrs) {
        
            //var form = cg.getPropertyOrDefault(attrs, "cgForm", "ciForm");
           // var field = cg.getPropertyOrDefault(attrs, "cgField", hpo);
            //var errors = cg.getPropertyOrDefault(attrs, "cgErrorMessages", "clinicalInfoHpoMessages");
            //return cgDirectives.inputTemplateSelect(form, field, errors, errors, "cg-hpo=''", "Select hpo terms", element);
          return '<input type="text" style="width:380px" name="'+attrs.name+'" jso-category="" id="'+attrs.id+'" ></input>';
          
        }
      
    }
});

module.directive('jsoCategory',['hcService','$http', function (hcService, $http) {
  return {
        restrict: 'EA',
        require: 'ngModel',
        link: function (scope, element, attrs, ngModel) {
           
            var selectParams = hcService.getRemoteMultiPagedConfig1(element, ngModel, 'Select category', true, "/getcategory", 5, {});
                     
            hcService.generateSelect2Box1(element, selectParams, scope, ngModel, attrs.ngModel);
           
        }
    };
}]);

module.directive('ngSparkline', function() {
	  return {
	    restrict: 'E',
	    template: '<div class="sparkline">fgfgfgfg</div>'
	  }
	});

module.directive('hcCategoryTreeDiv', ['hcService', function (hcService) {
    return {
        restrict: 'E',
        replace: true,
        template: function (element, attrs) {
        
            
            //var errors = cg.getPropertyOrDefault(attrs, "cgErrorMessages", "clinicalInfoHpoMessages");
            return '<div  id="categoryTree" name="categoryTree"></div>';//cgDirectives.inputTemplateSelect(form, field, errors, errors, "cg-hpo=''", "Select hpo terms", element);
        },
        link: function (scope, element, attrs, ngModel) {
            hcService.generateDynatree(element,scope, ngModel, attrs.url);
            
        }
    }
}]);

module.directive('jsoCkEditor', function () {
    return {
        restrict: 'EA',
        replace: true,
        require: '?ngModel',
        template: function (element, attrs) {
            
            return '<textarea id="contentEditor"></textarea>';
        },
        link: function (scope, element, attrs, ngModel) {
          var ck = CKEDITOR.replace(element[0], {height: 250});

            /*if (!ngModel){
              return;
            }

            ck.on('pasteState', function() {
              scope.$apply(function() {
                ck.removeAllListeners();
                CKEDITOR.remove(ck);
                ngModel.$setViewValue(ck.getData());

              });
            });

            ngModel.$render = function(value) {
              ck.setData(ngModel.$viewValue);
            };*/

               if (!ngModel) return;

              ck.on('instanceReady', function() {
                ck.setData(ngModel.$viewValue);
              });

              function updateModel() {
                  scope.$apply(function() {
                      ngModel.$setViewValue(ck.getData());
                  });
              }

              ck.on('change', updateModel);
              ck.on('key', updateModel);
              ck.on('dataReady', updateModel);

              ngModel.$render = function(value) {
                ck.setData(ngModel.$viewValue);
              };
        }
    }
});
/*module.directive('shCk', function () {
    return {
        restrict: 'A',
        require: 'ngModel',
        link: function (scope, element, attrs, ngModel) {
          var ck = CKEDITOR.replace(element[0],{toolbar : 'Basic'});

            if (!ngModel){
              return;
            }

            ck.on('pasteState', function() {
              scope.$apply(function() {
                ngModel.$setViewValue(ck.getData());
              });
            });

            ngModel.$render = function(value) {
              ck.setData(ngModel.$viewValue);
            };
        }
    };
});*/

