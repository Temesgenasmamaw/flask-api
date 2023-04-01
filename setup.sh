mkdir -p ~/.flask/

echo "\
[general]\n\
email = \"your-email@domain.com\"\n\
" > ~/.flask/credentials.toml

echo "\
[server]\n\
headless = true\n\
enableCORS=false\n\
port = $PORT\n\
" > ~/.flask/config.toml