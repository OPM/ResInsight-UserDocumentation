# docs/source/_ext/hide_grpc_params.py
from sphinx.ext.autodoc import ClassDocumenter
import inspect

class CustomClassDocumenter(ClassDocumenter):
    def format_signature(self, **kwargs):
        # Get the original signature
        sig = super().format_signature(**kwargs)
        
        # Remove gRPC parameters from all class signatures
        if sig and ('pb2_object' in sig or 'channel' in sig):
            # Replace with empty parentheses
            return '()'
        
        return sig

def setup(app):
    app.add_autodocumenter(CustomClassDocumenter, override=True)
    return {
        'version': '0.1',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }