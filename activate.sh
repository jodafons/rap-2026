
export VIRTUALENV_NAMESPACE='.itm-env'
export LOGURU_LEVEL="DEBUG"
export VIRTUALENV_PATH=$PWD/$VIRTUALENV_NAMESPACE
export ITM_DATA_PATH=$PWD/data


# NOTE: this came from https://hub.cognite.com/open-industrial-data-211/openid-connect-on-open-industrial-data-993
export COGNITE_CLIENT_ID="put_your_token_here"

if [ -d "$VIRTUALENV_PATH" ]; then
    echo "$VIRTUALENV_PATH exists."
    source $VIRTUALENV_PATH/bin/activate
else
    virtualenv -p python ${VIRTUALENV_PATH}
    source $VIRTUALENV_PATH/bin/activate
    pip install -e .
fi
