from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DecimalField, IntegerField,\
    TextAreaField, SelectField, PasswordField
from wtforms.fields.html5 import EmailField
from flask_wtf.file import FileField
from wtforms.validators import Required
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, TextAreaField, FileField, SelectField,RadioField
from wtforms import FloatField
from wtforms.validators import DataRequired, Email, Length, ValidationError,AnyOf
from wtforms.fields.html5 import DateField
from flask_wtf.file import FileField, FileRequired
from wtforms.fields.html5 import EmailField
from wtforms.validators import Required

def validar_obvio(form,field):
    if field.data=="12345678":
        raise ValidationError('La clave debe ser más segura!!')

class Publicaciones(FlaskForm):
    post = TextAreaField('Notas de las fotos', validators=[
        DataRequired(), Length(min=1, max=140)
    ])
    imagen = FileField('image')
 
    submit = SubmitField('Subir')

class FormArticulo(FlaskForm):
    nombre = StringField("Nombre:",
                         validators=[Required("Tienes que introducir el dato")]
                         )
    precio = DecimalField("Precio:", default=0,
                          validators=[Required("Tienes que introducir el dato")
                                      ])
    iva = IntegerField("IVA:", default=21,
                       validators=[Required("Tienes que introducir el dato")])
    descripcion = TextAreaField("Descripción:")
    photo = FileField('Selecciona imagen:')
    stock = IntegerField("Stock:", default=1,
                         validators=[Required("Tienes que introducir el dato")]
                         )
    CategoriaId = SelectField("Categoría:", coerce=int)
    submit = SubmitField('Enviar')

class FormSINO(FlaskForm):
    si = SubmitField('Si')
    no = SubmitField('No')



class buscapac(FlaskForm):
    iden = StringField('Cédula Pasaporte', validators=[DataRequired()],render_kw={"placeholder": "Identificación"})
    nombres = StringField('Nombres', validators=[DataRequired()])
    fec_nac = DateField('Fecha de Nacimiento', validators=[DataRequired()],render_kw={"placeholder": "Fecha de Nacimiento"})
    fec_compra = DateField('Fecha de Ingreso', validators=[],render_kw={"placeholder": "Fecha de compra"})
    telefono1 = StringField('Teléfono Domicilio', validators=[])

    submit = SubmitField('Enviar')

class buscxc(FlaskForm):
    iden = StringField('Cliente', validators=[DataRequired()], render_kw={"placeholder": "Cliente"})
    fec_ini = DateField('Fecha inicio', validators=[DataRequired()],render_kw={"placeholder": "Fecha inicio"})
    fec_fin = DateField('Fecha fin', validators=[],render_kw={"placeholder": "Fecha fin"})
    submit = SubmitField('Buscar')


class LoginForm(FlaskForm):
    username = StringField('User', validators=[Required()])
    password = PasswordField('Password', validators=[Required()])
    submit = SubmitField('Entrar')


class FormUsuario(FlaskForm):
    username = StringField('Login', validators=[Required()])
    password = PasswordField('Password', validators=[Required()])
    nombre = StringField('Nombre completo')
    email = EmailField('Email')
    submit = SubmitField('Aceptar')


class alumno(FlaskForm):
    iden = StringField('Cédula Pasaporte', validators=[DataRequired()],render_kw={"placeholder": "Identificación"})
    nombres = StringField('Nombres', validators=[DataRequired()])
    fec_nac = DateField('Fecha de Nacimiento', validators=[DataRequired()],render_kw={"placeholder": "Fecha de Nacimiento"})
    fec_compra = DateField('Fecha de Ingreso', validators=[],render_kw={"placeholder": "Fecha de compra"})
    telefono1 = StringField('Teléfono Domicilio', validators=[])

    submit = SubmitField('Enviar')


class datos_alumno(FlaskForm):
    iden = StringField('Cédula Pasaporte', validators=[DataRequired()],render_kw={"placeholder": "Identificación"})
    cinturon = StringField('Cinturón', validators=[])
    peso = StringField('Peso Kg', validators=[])
    estatura = StringField('Estatura cm', validators=[])
    flexibilidad = StringField('Nivel de flexibilidad', validators=[])
       
    submit = SubmitField('Enviar')

class campeonato(FlaskForm):
    nombre = StringField('Nombre', validators=[DataRequired()])
    puntua = SelectField('Es Puntuable',choices=[('S', 'Si'), ('N', 'No'),],default = 'C',render_kw={}, id='est_civil')
    fecha = DateField('Fecha del evento', validators=[DataRequired()],render_kw={"placeholder": "Fecha del evento"})
    obs  = StringField('Observacones',validators=[])
       
    submit = SubmitField('Enviar')

class campeonato_combate(FlaskForm):
    iden = IntegerField('Identificación', validators=[DataRequired()])
    nombre = StringField('Nombre del Campeonato', validators=[DataRequired()])
    puntua = SelectField('Es Puntuable',choices=[('S', 'Si'), ('N', 'No'),],default = 'C',render_kw={}, id='est_civil')
    fecha = DateField('Fecha del evento', validators=[DataRequired()],render_kw={"placeholder": "Fecha del evento"})
    ubicacion = SelectField('Medalla Obtenida',choices=[('Oro', 'Oro'), ('Plata', 'Plata'),('Bronce', 'Bronce'), ('Cuarto', 'Cuarto'),('Sin Podio', 'Sin Podio')],default = '',render_kw={}, id='medalla')
    cinturon = StringField('Cinturon', validators=[DataRequired()])
    edad = StringField('Edad', validators=[DataRequired()])
    peso = StringField('Peso', validators=[DataRequired()])
    num_part = IntegerField('Número de participantes', validators=[DataRequired()],render_kw={"placeholder": ""})
    obs  = StringField('Observacones',validators=[])
       
    submit = SubmitField('Enviar')


class campeonato_pommse(FlaskForm):
    iden = IntegerField('Identificación', validators=[DataRequired()])
    nombre = StringField('Nombre del Campeonato', validators=[DataRequired()])
    puntua = SelectField('Es Puntuable',choices=[('S', 'Si'), ('N', 'No'),],default = 'C',render_kw={}, id='est_civil')
    fecha = DateField('Fecha del evento', validators=[DataRequired()],render_kw={"placeholder": "Fecha del evento"})
    ubicacion = SelectField('Medalla Obtenida',choices=[('Oro', 'Oro'), ('Plata', 'Plata'),('Bronce', 'Bronce'),('Cuarto', 'Cuarto'),('Sin Podio', 'Sin Podio')],default = '',render_kw={}, id='medalla')
    cinturon = StringField('Cinturon', validators=[DataRequired()])
    edad = StringField('Edad', validators=[DataRequired()])
    num_part = IntegerField('Número de participantes', validators=[DataRequired()],render_kw={"placeholder": ""})
    obs  = StringField('Observacones',validators=[])
       
    submit = SubmitField('Enviar')

class fechas_buscar(FlaskForm):
    mes = SelectField(u'Mes', choices=[(1, 'Enero'), (2, 'Febrero'), (3, 'Marzo'), (4, 'Abril'), (5, 'Mayo'), (6, 'Junio'), (7, 'Julio'), (8, 'Agosto'), (9, 'Septiembre'), (10, 'Octubre'),(11, 'Noviembre'),(12, 'Diciembre')], default='1', render_kw={}, id='mes_buscar')
    fec_fin = DateField('Fecha de Final', validators=[DataRequired()],render_kw={"placeholder": "Fecha Final"})
    iden = StringField('Cédula Pasaporte', validators=[],render_kw={"placeholder": "Identificación"})

   
    submit = SubmitField('Enviar')


class FormChangePassword(FlaskForm):
    password = PasswordField('Password', validators=[Required()])
    submit = SubmitField('Aceptar')


class UploadForm(FlaskForm):
    photo = FileField('selecciona imagen:',validators=[FileRequired()])
    submit = SubmitField('Submit')


class horario_ent(FlaskForm):
    iden = IntegerField('Identificación', validators=[DataRequired()])
    horario = SelectField('Horario',choices=[('09:00-10:30', '09:00-10:30'), ('15:30-17:00', '15:30-17:00'),('17:00-18:30', '17:00-18:30'),('18:30-20:00', '18:30-20:00')],default = '',render_kw={}, id='horario')

    submit = SubmitField('Submit')


class Upload_excel(FlaskForm):
    mens = StringField('Mensaje', validators=[],render_kw={"placeholder": ""})
    
    submit = SubmitField('Submit')