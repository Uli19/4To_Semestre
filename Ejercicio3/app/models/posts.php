<?php

namespace app\models;

class posts extends Model {

    protected $table;
    protected $fillable = [
        'userId',
        'title',
        'body'
    ];
    public $values = [];

    public function __construct(){
        parent::__construct();
        $this->table = $this->connect();
    }

    public function getAllPosts($limit = 5){
        //$result = $this->all()->get();
        $result = $this->select(['title', 'date_format(created_at, "%d/%m/%Y") as fecha', 'b.name'])
                        ->join('user b','a.userId=b.id' )
                        ->where([['active', 1]])
                        ->orderBy([['created_at', 'DESC']])
                        ->limit($limit)
                        ->get();
        return $result;
    }

}

?>