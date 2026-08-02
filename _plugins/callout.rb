#!/usr/bin/env ruby
#
# Convert GitHub Flavored Markdown / Obsidian callout syntax
# (e.g. `> [!NOTE]`, `> [!TIP]`, `> [!WARNING]`) into Chirpy prompt blocks.
#
# The callout syntax is rendered by kramdown as a plain `<blockquote>` with the
# `[!TYPE]` marker left as literal text. This hook post-processes the rendered
# HTML and turns such blockquotes into `<blockquote class="prompt-...">` blocks,
# reusing the theme's built-in prompt styles.

module CalloutConverter
  # Map callout type (case-insensitive) to a Chirpy prompt class suffix.
  TYPE_MAP = {
    'note'      => 'note',
    'tip'       => 'tip',
    'important' => 'important',
    'warning'   => 'warning',
    'caution'   => 'caution',
    'danger'    => 'danger',
    'info'      => 'info',
    'success'   => 'success',
    'question'  => 'question',
    'example'   => 'example',
    'failure'   => 'failure',
    'bug'       => 'bug'
  }.freeze

  # Regex matching the `[!TYPE]` marker (optionally followed by a title).
  MARKER_RE = /\[!\s*([A-Za-z]+)\s*\]\s*/

  def self.convert(html)
    html.gsub(%r{<blockquote>([\s\S]*?)</blockquote>}) do |match|
      inner = Regexp.last_match(1)

      if (m = inner.match(MARKER_RE))
        type = m[1].downcase
        prompt_class = TYPE_MAP[type] || 'note'

        # Remove the `[!TYPE]` marker (and any trailing whitespace) from the
        # first paragraph. The marker may appear at the start of a `<p>` tag.
        cleaned = inner.sub(MARKER_RE, '')

        "<blockquote class=\"prompt-#{prompt_class}\">#{cleaned}</blockquote>"
      else
        match
      end
    end
  end
end

Jekyll::Hooks.register %i[posts pages], :post_render do |doc|
  next if doc.output.nil?

  doc.output = CalloutConverter.convert(doc.output)
end
