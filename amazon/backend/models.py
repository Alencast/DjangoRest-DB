from django.db import models

class Usuario(models.Model):
    id = models.AutoField(primary_key=True)

    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefone = models.CharField(max_length=15, blank=True, null=True)
    data_cadastro = models.DateTimeField(auto_now_add=True)    

    def __str__(self):
        return f'{self.nome} - {self.email}'
    

class LiderEscala(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    hospital = models.CharField(max_length=100)
    data_cadastro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.nome} - {self.hospital}'
    
class Livros(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=100)
    ano_de_publicacao = models.IntegerField()
    genero = models.CharField(max_length=50)

class Autores(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    data_nascimento = models.DateField()
    nacionalidade = models.CharField(max_length=50)

class Usuarios(models.Model):
    
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    data_de_registro = models.DateTimeField(auto_now_add=True)


class Emprestimos(models.Model):
    livro = models.ForeignKey(Livros, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuarios, on_delete=models.CASCADE)
    data_emprestimo = models.DateTimeField(auto_now_add=True)
    data_devolucao = models.DateTimeField(blank=True, null=True)


class Reservas(models.Model):
    livro = models.ForeignKey(Livros, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuarios, on_delete=models.CASCADE)
    data_reserva = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=[('pendente', 'Pendente'), ('concluida', 'Concluída'), ('cancelada', 'Cancelada')])


class Multas(models.Model):
    usuario = models.ForeignKey(Usuarios, on_delete=models.CASCADE)
    valor = models.DecimalField(max_digits=6, decimal_places=2)
    data_multa = models.DateTimeField(auto_now_add=True)
    paga = models.BooleanField(default=False)

class Categorias(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=50)
    descricao = models.TextField(blank=True, null=True)

class Editoras(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    endereco = models.CharField(max_length=200, blank=True, null=True)
    telefone = models.CharField(max_length=15, blank=True, null=True)
