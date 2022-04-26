<?php
class Conexion{
    public static function conexionBD(){
        $host='localhost';
        $dbname='insert';
        $username='root';
        $pasword='';

        try{
            $conn = new PDO("mysql:host=$host;dbname=$dbname",$username,$pasword);
            echo"se conecto correctamente a la base de datos";
        }catch(PDOException $exp){
            echo("no se logro conectar con la base de datos:$dbname, error:$exp");
        }
        return$conn;
}

}

?>