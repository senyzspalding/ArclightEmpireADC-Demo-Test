<% manifest_url = @document['dado_identifier_ssm']&.first %>
<% action = @document['dado_action_ssm']&.first %>

<% if action&.downcase == "embed" && manifest_url.present? %>
  <div class="mirador-container mb-3" id="mirador-container" style="height: 600px; position: relative; overflow: hidden;"></div>
<% elsif manifest_url.present? %>
  <a class="plain_link" href="<%= manifest_url %>"><%= @resource.label %></a>
<% end %>

<%= javascript_include_tag "https://unpkg.com/mirador@4/dist/mirador.min.js" %>
<script>
  document.addEventListener('DOMContentLoaded', () => {
    const miradorContainer = document.getElementById('mirador-container');
    if (!miradorContainer) return;

    const viewer = Mirador.viewer({
      id: 'mirador-container',
      windows: [{
        loadedManifest: '<%= manifest_url %>',
        canvasIndex: 0
      }]
    });
  });
</script>
