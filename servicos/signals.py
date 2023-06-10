import cloudinary.api
from django.db.models.signals import pre_delete
from django.dispatch import receiver


@receiver(pre_delete)
def excluir_img_cloudinary(sender, instance, **kwargs):
    if sender.__name__ == 'Servico':
        if instance.imagem:
            chave_publica_imagem = instance.imagem.public_id
            cloudinary.api.delete_resources(chave_publica_imagem)

        if instance.video:
            chave_publica_video = instance.video.public_id
            cloudinary.api.delete_resources(chave_publica_video)

        # Todo: exclusão do video não funcionou
