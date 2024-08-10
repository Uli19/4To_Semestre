<?php

namespace app\controllers;

use app\classes\View;

class ErrorController extends Controller{
    public function __construct(){
        parent::__construct();
    }

    public function error404() {
        $response =[
            'title' => "Error: no encontrado",
            'code' => 404
        ];

        View::render("error", $response);
    }

}
