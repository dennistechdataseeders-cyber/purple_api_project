from rest_framework.renderers import BrowsableAPIRenderer

class BrowsableAPIRendererWithAPIKey(BrowsableAPIRenderer):
    def get_custom_rendered_html_form(self, data, view, method, request):
        html = super().get_custom_rendered_html_form(data, view, method, request)

        # Add an input for the API key
        extra = """
        <div class="form-group">
            <label>API Key</label>
            <input name="HTTP_X_API_KEY" type="text" class="form-control" placeholder="Enter API Key">
        </div>
        """

        return extra + html