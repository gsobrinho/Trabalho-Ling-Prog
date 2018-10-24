rom flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, IntegerField
from wtforms.validators import DataRequired

class LoginForm(Form):
   
  
  linha de pesquisa = StringField("linha de pesquisa", validators = [DataRequires()])
  nome = StringField("nome", validators = [DataRequires()])
  pai = StringField("pai", validators = [DataRequires()])
  mae = StringField("mae", validators = [DataRequires()])
  cpf = StringField("cpf", validators = [DataRequires()])
  birthdate = StringField("birthdate", validators = [DataRequires()])
  sexo = StringField("sexo", validators = [DataRequires()])
  nacionalidade = StringField("nacionalidade", validators = [DataRequires()])
  pais = StringField("pais", validators = [DataRequires()])
  anochegada = StringField("anochegada", validators = [DataRequires()])
  logradouro = StringField("logradouro", validators = [DataRequires()])
  numero = StringField("numero", validators = [DataRequires()])
  complemento = StringField("complemento")
  bairro = StringField("bairro", validators = [DataRequires()])
  municipio = StringField("municipio", validators = [DataRequires()])
  UF = StringField("UF", validators = [DataRequires()])
  cep = IntegerField("cep", validators = [DataRequires()])
  telcasa = IntegerField("telcasa")
  celular = IntegerField("celular", validators = [DataRequires()])
  email = StringField("email", validators = [DataRequires()])
  tempo = StringField("tempo", validators = [DataRequires()])
  justificativa = StringField("justificativa", validators = [DataRequires()])
  justificativaoutros = StringField("justificativaoutros")
  empresa = StringField("empresa")
  funcao = StringField("funcao")
  telefoneempresa = StringField("telefoneempresa")
  emailempresa = StringField("emailempresa")
  rg = StringField("rg", validators = [DataRequires()])
  dattarg = StringField("dattarg", validators = [DataRequires()])
  orgaorg = StringField("orgaorg", validators = [DataRequires()])
  estadorg = StringField("estadorg", validators = [DataRequires()])
  faculdade = StringField("faculdade", validators = [DataRequires()])
  curso = StringField("curso", validators = [DataRequires()])
  estadocurso = StringField("estadocurso", validators = [DataRequires()])
  anoconclusao = StringField("anoconclusao", validators = [DataRequires()])
  cartainteresse = StringField("cartainteresse", validators = [DataRequires()])
  
  
  
  
  
  