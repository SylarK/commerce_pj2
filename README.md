# Project II

Este projeto teve por objetivo a composição da nota no curso proposto pela HarvardX (Web Programming with Python and Javascript).

##### Conteúdo

`` O projeto em questão utiliza Django (Py), HTML, CSS, Sql para apresentar a estrutura de um website que funcionará como uma espécie de site de leilão. A ideia seria mais ou menos do que acontece em plataformas como enjoei.com, desapega.com, olx.com etc só que com uma visão mais para o lado de leilão. Ou seja, o usuário poderá realizar o cadastramento de um item e realizar o leilão de tal item.``

* [x] **Models**: A aplicação deverá ter no mínimo três models, uma para as **'auctions listings'**, uma para **'bids'** e outra para os **comentários** feitos nas 'auctions listings'.

* [x] **Create Listing**: O usuário deverá ser capaz de ter acesso a página que possibilita que o mesmo crie uma nova lista. Ele deverá espicificar o título, um texto de descrição e o valor de início do leilão. Opcionalmente o usuário deverá ser capaz de adicionar uma URL de uma imagem e/ou uma categoria.

* [x] **Active Listings Page**: A rota padrão da aplicação deverá mostrar aos usuários a lista com todos os itens de leilão que estão ativos no momento. Para cada item ativo a página inicial deverá mostrar pelo menos **title, description, current price, and photo (se a mesma existir)**.

* [x] **Listing Page**: Clicando em determinado item o usuário deverá ser direcionado a uma página em que o mesmo visualizará o item em específico. Nessa página os usuários são capazes de visualizar todos os detalhes do item, incluindo o preço atual do item.

    * [ ] Se o usuário estiver logado, será capaz de adicionar o item ao Watchlist. Se o item já estiver lá ele poderá remove-lo.

    * [x] Se o usuário estiver logado, poderá ser capaz de realizar um lance (que deverá ser maior do que o valor atual)

    * [ ] Se o usuário estiver logado e for o criador do leilão daquele item, poderá realizar o fechamento do leilão, declarando o último lance como ganhador e deixando aquele item indisponível para outras visualizações.

    * [ ] Se o usuário vencedor do item específico do leilão for o ganhador e acessar a página, a página deverá notifica-lo.

    * [x] Usuários que estão logados deverão ser capazes de realizar comentários, e os comentários deverão estar listados no decorrer da página.

* [ ] **Watchlist**: Usuários que estão logados são capazes de visitar a página de Watchlist que mostrará todos os itens que o usuário adicionou em sua página. Clicando em uma dessas o usuário será redirecionado a esta página.

* [ ] **Categorias**: Usuários serão capazes de visitar uma página que listará todas as categorias. Clicando no nome da categoria será mostrado todos os itens de leilão ativos daquela categoria.

* [ ] **Django Admin Interface**: Através do Django Admin Interface, o administrador do site deverá ser capaz de visualizar, editar e deletar qualquer 'listings, comments, and bids' feitos no site.


##### Content (English): 

* **Models**: Your application should have at least three models in addition to the User model: one for auction listings, one for bids, and one for comments made on auction listings. It’s up to you to decide what fields each model should have, and what the types of those fields should be. You may have additional models if you would like.

* **Create Listing**: Users should be able to visit a page to create a new listing. They should be able to specify a title for the listing, a text-based description, and what the starting bid should be. Users should also optionally be able to provide a URL for an image for the listing and/or a category (e.g. Fashion, Toys, Electronics, Home, etc.).

* **Active Listings Page**: The default route of your web application should let users view all of the currently active auction listings. For each active listing, this page should display (at minimum) the title, description, current price, and photo (if one exists for the listing).

    *   Listing Page: Clicking on a listing should take users to a page specific to that listing. On that page, users should be able to view all details about the listing, including the current price for the listing.

    *   If the user is signed in, the user should be able to add the item to their “Watchlist.” If the item is already on the watchlist, the user should be able to remove it.

    *   If the user is signed in, the user should be able to bid on the item. The bid must be at least as large as the starting bid, and must be greater than any other bids that have been placed (if any). If the bid doesn’t meet those criteria, the user should be presented with an error.

    *   If the user is signed in and is the one who created the listing, the user should have the ability to “close” the auction from this page, which makes the highest bidder the winner of the auction and makes the listing no longer active.

    *   If a user is signed in on a closed listing page, and the user has won that auction, the page should say so.

    *   Users who are signed in should be able to add comments to the listing page. The listing page should display all comments that have been made on the listing.

* **Watchlist**: Users who are signed in should be able to visit a Watchlist page, which should display all of the listings that a user has added to their watchlist. Clicking on any of those listings should take the user to that listing’s page.

* **Categories**: Users should be able to visit a page that displays a list of all listing categories. Clicking on the name of any category should take the user to a page that displays all of the active listings in that category.

* **Django Admin Interface**: Via the Django admin interface, a site administrator should be able to view, add, edit, and delete any listings, comments, and bids made on the site.

