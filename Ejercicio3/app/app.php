<?php

    namespace app;

    use app\classes\AutoLoader as AutoLoader;
    use app\classes\Router as Router;

error_reporting(E_ALL);
ini_set('display_errors', 1);

class App {
    public function __construct() {
        $this->init();
        $this->loadFunctions();
        $this->initAutoLoader();
        $this->initRouter();
    }

    private function init(){
        $this->initConfig(); 
    }

    private function initConfig(){
        if(!file_exists(__DIR__ . '/config.php')){
            die('No se encontró el archivo de configuración config.php');            
        }
        require_once __DIR__ . '/config.php';
    }

    private function loadFunctions(){
        if(!file_exists(FUNCTIONS . 'main_functions.php')){
            die('No se encontró el archivo de funciones de usuario main_functions.php');
        }
        require_once FUNCTIONS . 'main_functions.php';
    }

    private function initAutoLoader(){
        if(!file_exists(CLASSES . 'AutoLoader.php')){
            die('No se encontró la clase AutoLoader.php');
        }
        require_once CLASSES . 'AutoLoader.php';
        AutoLoader::register();
        return;
    }

    private function initRouter(){
        if(!file_exists(CLASSES . 'Router.php')){
            die('No se encontró la clase Router.php');
        }
        require_once CLASSES . 'Router.php';
        $router = new Router();
        $router->route();
    }

    public static function run(){
        $app = new self();
        return;
    }
}

?>