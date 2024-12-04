<?php
include_once 'php_action/db_connect.php';
include_once 'includes/header.php';
include_once 'includes/message.php';
?>



<div class="row">
    <div class="col s12 m6 push-m3 ">
        <h3 class="light"> Clientes</h3>


<table>
        <thead>
            <tr>
                <th>Nome:</th> 
                <th>Sobrenome:</th> 
                <th>E-mail:</th> 
                <th>Idade:</th> 
            </tr>
        </thead>
        <tbody>
            <?php
            $sql = "SELECT * FROM clientes";
            $resultado = mysqli_query($connect, $sql);
            
            while ($dados = mysqli_fetch_array($resultado)):
            ?>
                <tr>
                <td><?php echo $dados['nome'] ;?></td> 
                <td><?php echo $dados['sobrenome'] ;?></td> 
                <td><?php echo $dados['email'] ;?></td> 
                <td><?php echo $dados['idade'] ;?></td>

                <td><a href="editar.php?id=<?php echo $dados['id'];?>" class="btn-floating purple"><i class="material-icons">
                edit</i></a></td>
                <td><a href="#modal<?php echo $dados['id'];?>" class="btn-floating purple modal-trigger"><i class="material-icons">
                delete</i></a></td> 
                <!-- Modal Structure -->
                <div id="modal<?php echo $dados['id'];?>" class="modal">
                <div class="modal-content">
                <h4>opa!</h4>
                <h4>tem certeza que deseja excluir esse cliente?</h4>
                </div>
                <div class="modal-footer">
                <form action="php_action/delete.php" method="POST">
                    <input type="hidden" name="id" value="<?php echo $dados['id'];?>">
                    <button type="submit" name="btn-deletar" class="btn red" >sim eu quero deletar"</button>

                    <a href="#!" class="modal-close waves-effect waves-green btn-flat">Cancelar</a>

                </div>
                </div>


            </tr>
            <?php endwhile; ?>
            
        </tbody>
</table>
    <br>
    <a href="adicionar.php" class="btn purple">adicionar novo cliente</a>
    
    
    </div>
   
</div>



<?php
include_once 'includes/footer.php';
?>


<!--Sarah_2int1-->