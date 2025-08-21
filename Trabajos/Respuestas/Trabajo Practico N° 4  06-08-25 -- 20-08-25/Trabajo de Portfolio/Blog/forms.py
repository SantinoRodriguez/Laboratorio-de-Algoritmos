from django import forms
from .models import Post, Comment

class PostForm(forms.ModelForm):
    """
    Formulario para crear y editar posts del blog
    """
    class Meta:
        model = Post
        fields = ('title', 'text', 'image')
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Título del post',
                'maxlength': '200'
            }),
            'text': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Contenido del post...',
                'rows': 10,
                'style': 'resize: vertical;'
            }),
            'image': forms.FileInput(attrs={
                'class': 'form-control-file',
                'accept': 'image/*'
            })
        }
        labels = {
            'title': 'Título',
            'text': 'Contenido',
            'image': 'Imagen (opcional)'
        }
        help_texts = {
            'title': 'Máximo 200 caracteres',
            'text': 'Puedes usar texto plano, se convertirán los saltos de línea automáticamente',
            'image': 'Formatos aceptados: JPG, PNG, GIF. Tamaño máximo recomendado: 2MB'
        }

    def clean_title(self):
        """
        Validación personalizada para el título
        """
        title = self.cleaned_data.get('title')
        if title and len(title.strip()) < 5:
            raise forms.ValidationError('El título debe tener al menos 5 caracteres.')
        return title.strip() if title else title

    def clean_text(self):
        """
        Validación personalizada para el contenido
        """
        text = self.cleaned_data.get('text')
        if text and len(text.strip()) < 20:
            raise forms.ValidationError('El contenido debe tener al menos 20 caracteres.')
        return text


class CommentForm(forms.ModelForm):
    """
    Formulario para agregar comentarios a los posts
    """
    class Meta:
        model = Comment
        fields = ('author', 'text')
        widgets = {
            'author': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Tu nombre',
                'maxlength': '200'
            }),
            'text': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Escribe tu comentario...',
                'rows': 4,
                'style': 'resize: vertical;'
            })
        }
        labels = {
            'author': 'Nombre',
            'text': 'Comentario'
        }
        help_texts = {
            'author': 'Nombre que aparecerá en el comentario',
            'text': 'Comparte tu opinión de manera respetuosa'
        }

    def clean_author(self):
        """
        Validación personalizada para el nombre del autor
        """
        author = self.cleaned_data.get('author')
        if author and len(author.strip()) < 2:
            raise forms.ValidationError('El nombre debe tener al menos 2 caracteres.')
        
        # Filtrar palabras ofensivas básicas (puedes expandir esta lista)
        palabras_prohibidas = ['spam', 'bot', 'admin', 'administrador']
        if author and any(palabra in author.lower() for palabra in palabras_prohibidas):
            raise forms.ValidationError('Ese nombre no está permitido.')
        
        return author.strip() if author else author

    def clean_text(self):
        """
        Validación personalizada para el texto del comentario
        """
        text = self.cleaned_data.get('text')
        if text and len(text.strip()) < 10:
            raise forms.ValidationError('El comentario debe tener al menos 10 caracteres.')
        
        # Verificar que no sea solo espacios o caracteres especiales
        if text and not any(char.isalnum() for char in text):
            raise forms.ValidationError('El comentario debe contener texto válido.')
        
        return text.strip() if text else text


# Formulario adicional para búsqueda (opcional)
class SearchForm(forms.Form):
    """
    Formulario simple para búsqueda de posts
    """
    query = forms.CharField(
        max_length=200,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Buscar posts...',
            'type': 'search'
        }),
        label='Buscar',
        required=True
    )
    
    def clean_query(self):
        query = self.cleaned_data.get('query')
        if query and len(query.strip()) < 3:
            raise forms.ValidationError('La búsqueda debe tener al menos 3 caracteres.')
        return query.strip() if query else query