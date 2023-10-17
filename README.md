# TestingTask
Django-app, который позволяет вносить в БД меню (одно или несколько) через админку, и нарисовать на любой нужной странице меню по названию,
также при клике на меню происходит переход по заданному в нем URL. URL может быть задан как явным образом, так и через named url (заранее заданых через справочник).
На отрисовку каждого меню требуется ровно 1 запрос к БД (prefetch_related).
Активный пункт меню определяется исходя из URL текущей страницы (активный элемент подсвечивается специальным фоном).
Хранится во встроенной БД.
Меню редактируется в стандартной админке Django.
Меню реализовано через использование template tag.
