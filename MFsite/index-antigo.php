<?php
//conexao
include_once 'phpaction/db_connect.php';
//header
include_once 'includes/header.php';
//message
include_once 'includes/message.php';
?>

<div class= "row">
    <div class="col s12 m8 push-m2">
        <h3 class="light"> Clientes </h3>
        <table class="striped">
            <thead>
                <tr>
                    <th> Nome:</th>
                    <th> Sobrenome:</th>
                    <th> Email:</th>
                    <th> Idade:</th>
                </tr>
            </thead>
            
            <tbody>
                <?php
                $sql = "SELECT * FROM clientes";
                $resultado = mysql_query ($connect, $sql);

                if (mysqli_num_rows($resultado) > 0):
                
                while($dados = mysqli_fetch_array($resultado)):
                    ?>
                    <tr>
                        <td><?php echo $dados['nome'];?></td>
                        <td><?php echo $dados['sobrenome'];?></td>
                        <td><?php echo $dados['email'];?></td>
                        <td><?php echo $dados['idade'];?></td>
                        <td><a href="editar.php?id<?php echo $dados['id'];?>"
class="btn-=floating orange"><i class="material-icons">edit</i></a></td>

<td><a href= "#modal>?php echo $dados ['id']; ?>"
  class="btn-floating red modal-trigger">
                    <i class="material-icons">delete</i></a></td>

                    <!-- Modal Structure-->
                     <div id="modal<?php echo $dados['id']; ?>"
                     class="modal">
                     <div class="modal-content">
                        <h4>opa!</h4>
                        <p>  tem certeza que deseja excluir esse cliente</p>
                </div>
                    <div class="mada1-footer">
                        <form action="php_action/delete.php"method="post">
                            <input type="hidden" name= "id" value=" <?php echo $dados ["id"];?>">
                            <button type="submit">