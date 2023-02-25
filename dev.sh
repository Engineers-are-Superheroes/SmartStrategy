# Remove all build artifacts to make sure we do not rely on them
cd frontend
rm -r build
cd ../backend
rm -r static
cd ..

export DJANGO_ENV=development

echo
echo -e '\033[1mRun in another shell: cd frontend; npm start\033[0m'
echo
python backend/manage.py runserver