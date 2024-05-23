from django.db import models
from django.core.files import File
from io import BytesIO
import qrcode

class PublicPerson(models.Model):
    name = models.CharField(max_length=255)
    biography = models.TextField()
    works = models.TextField()
    photo = models.ImageField(upload_to='photos/')
    qr_code = models.ImageField(upload_to='qrcodes/', blank=True)

    def save(self, *args, **kwargs):
        # Сохраняем объект без QR-кода, чтобы получить self.id
        super().save(*args, **kwargs)
        
        # Генерируем QR-код
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        
        # Используем правильный URL
        qr.add_data(f'http://127.0.0.1:8000/person/{self.id}/')
        qr.make(fit=True)
        img = qr.make_image(fill='black', back_color='white')
        
        # Сохраняем QR-код в буфер
        buffer = BytesIO()
        img.save(buffer, format='PNG')
        buffer.seek(0)  # Сбрасываем указатель буфера в начало
        
        # Сохраняем файл QR-кода
        self.qr_code.save(f'{self.name}_qr.png', File(buffer), save=False)
        
        # Еще раз сохраняем объект с QR-кодом
        super().save(update_fields=['qr_code'])

