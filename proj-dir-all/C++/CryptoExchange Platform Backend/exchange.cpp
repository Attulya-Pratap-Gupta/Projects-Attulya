/*
Name: Attulya Pratap Gupta
Date: 4/30/2023
Title: Project 3
PID: 162198572
*/

// Including relevant files
#include "exchange.hpp"
#include "utility.hpp"
#include <set>

void Exchange::MakeDeposit(const std::string &username,
                           const std::string &asset, int amount) {
  //Function to make a deposit into user portfolios
  if (portfolio.find(username) == portfolio.end())
    portfolio[username][asset] = amount;
  else {
    if (portfolio[username].find(asset) == portfolio[username].end())
      portfolio[username][asset] = amount;
    else
      portfolio[username][asset] += amount;
  }
}

void Exchange::PrintUserPortfolios(std::ostream &os) const {
    //Function to print user portfolios
  os << "User Portfolios (in alphabetical order):" << std::endl;
  //Iterating through a 2-D map
  for (auto itr = portfolio.begin(); itr != portfolio.end(); itr++) {
    os << itr->first << "'s Portfolio: ";
    std::map<std::string, int> user = itr->second;
    for (auto ptr = user.begin(); ptr != user.end(); ptr++) {
      os << ptr->second << " " << ptr->first << ", ";
    }
    os << std::endl;
  }
}

bool Exchange::MakeWithdrawal(const std::string &username,
                              const std::string &assent, int amount) {
    //Making asset withdrawal from the portfolio
  if (portfolio.find(username) != portfolio.end()) {
    if (portfolio.at(username).find(assent) != portfolio.at(username).end()) {
      if (portfolio.at(username).at(assent) > amount) {
        portfolio.at(username).at(assent) -= amount;
        return true;
      } else if (portfolio.at(username).at(assent) == amount) {
        // Erasing key asset
        portfolio.at(username).erase(assent);
        return true;
      }
    }
  }
  return false;
}

bool Exchange::check_possible(const Order &pos, const std::string type) {
    //Checking if order is possible
  bool ans;
  if (type == "Buy")
    ans = MakeWithdrawal(pos.username, "USD",
                         static_cast<int>(pos.price * pos.amount));
  if (type == "Sell")
    ans = MakeWithdrawal(pos.username, pos.asset, pos.amount);
  return ans;
}

bool Exchange::AddOrder(const Order &current_order) {
    //Adding the order to be processed
  remove();
  bool possible = check_possible(current_order, current_order.side);
  if (possible == 0)
    return false;
  if (open_orders.size() > 0) {
    if (current_order.side == "Buy")
      buy_trade(current_order);
    if (current_order.side == "Sell")
      sell_trade(current_order);
  } else
    open_orders.push_back(current_order);
  return true;
}

void Exchange::buy_chrono(Order &element, Order &order) {
  if (element.price <= order.price) {
    if (element.amount >= order.amount) {
      element.amount -= order.amount;
      Trade new_order{order.username, element.username, order.asset,
                      order.amount, order.price};
      filled_orders.push_back({new_order});
      MakeDeposit(order.username, order.asset, order.amount);
      MakeDeposit(element.username, "USD", order.amount * order.price);
      order.amount = 0;
    }
    if (element.amount < order.amount) {
      order.amount -= element.amount;
      Trade new_order{order.username, element.username, order.asset,
                      element.amount, order.price};
      filled_orders.push_back({new_order});
      MakeDeposit(element.username, "USD", element.amount * order.price);
      MakeDeposit(order.username, order.asset, element.amount);
      element.amount = 0;
    }
  }
  // open_orders.push_back(order);
  // remove();
}

void Exchange::sell_chrono(Order &element, Order &order) {
  // element is buy type order is sell type
  if (element.price >= order.price) {
    if (element.amount >= order.amount) {
      element.amount -= order.amount;
      Trade new_order{element.username, order.username, order.asset,
                      order.amount, order.price};
      filled_orders.push_back({new_order});
      MakeDeposit(element.username, element.asset, order.amount);
      MakeDeposit(order.username, "USD", order.amount * order.price);
      order.amount = 0;
    }
    if (element.amount < order.amount) {
      order.amount -= element.amount;
      Trade new_order{element.username, order.username, order.asset,
                      element.amount, order.price};
      filled_orders.push_back({new_order});
      MakeDeposit(element.username, element.asset, element.amount);
      MakeDeposit(order.username, "USD", element.amount * order.price);
      element.amount = 0;
    }
  }
  // open_orders.push_back(order);
  // remove();
}

void Exchange::conduct_chrono_trade(Order &ord) {
  for (auto &elem : open_orders) {
    if (elem.side != ord.side && elem.asset == ord.asset) {
      if (ord.side == "Buy") {
        buy_chrono(elem, ord);
      }
      if (ord.side == "Sell") {
        sell_chrono(elem, ord);
      }
    }
  }
  if (ord.amount > 0) {
    open_orders.push_back(ord);
    // remove();
  }
}

void Exchange::remove() {
    //removing assets with zero amount
  for (auto &elem : open_orders) {
    if (elem.amount == 0)
      open_orders.erase(
          std::remove(open_orders.begin(), open_orders.end(), elem),
          open_orders.end());
  }
}

void Exchange::buy_trade(Order order) {
  Order lowest;
  lowest.amount = 0;
  lowest.price = 99999;
  for (auto &elem : open_orders) {
    if (elem.side != "Sell" || elem.asset != order.asset)
      continue;
    else {
      if (elem.price < lowest.price)
        lowest = elem;
    }
  }
  if (lowest.amount != 0) {
    if (lowest.amount >= order.amount && lowest.side != order.side &&
        lowest.asset == order.asset) {
      if (lowest.price <= order.price) {
        auto it = std::find(open_orders.begin(), open_orders.end(), lowest);
        it->amount -= order.amount;
        Trade new_order{order.username, lowest.username, order.asset,
                        order.amount, order.price};
        filled_orders.push_back({new_order});
        MakeDeposit(order.username, order.asset, order.amount);
        MakeDeposit(lowest.username, "USD", order.amount * order.price);
        order.amount = 0;
      }
    }
    if (lowest.amount < order.amount && lowest.side != order.side &&
        lowest.asset == order.asset) {
      if (lowest.price <= order.price) {
        order.amount -= lowest.amount;
        Trade new_order{order.username, lowest.username, order.asset,
                        lowest.amount, order.price};
        filled_orders.push_back({new_order});
        MakeDeposit(lowest.username, "USD", lowest.amount * order.price);
        MakeDeposit(order.username, order.asset, lowest.amount);
        auto it = std::find(open_orders.begin(), open_orders.end(), lowest);
        it->amount = 0;
      }
    }
  }
  // remove();
  if (order.amount > 0)
    conduct_chrono_trade(order);
}

void Exchange::sell_trade(Order order) {
  // Order is sell type //highest is buy type
  Order highest;
  highest.amount = 0;
  highest.price = 0;
  for (auto &elem : open_orders) {
    if (elem.side != "Buy" || elem.asset != order.asset)
      continue;
    else {
      if (elem.price > highest.price)
        highest = elem;
    }
  }
  if (highest.amount != 0) {
    if (highest.amount >= order.amount && highest.side != order.side &&
        highest.asset == order.asset) {
      if (highest.price >= order.price) {
        auto it = std::find(open_orders.begin(), open_orders.end(), highest);
        it->amount -= order.amount;
        Trade new_order{highest.username, order.username, order.asset,
                        order.amount, order.price};
        filled_orders.push_back({new_order});
        MakeDeposit(highest.username, order.asset, order.amount);
        MakeDeposit(order.username, "USD", order.amount * order.price);
        order.amount = 0;
      }
    }
    if (highest.amount < order.amount && highest.side != order.side &&
        highest.asset == order.asset) {
      if (highest.price >= order.price) {
        order.amount -= highest.amount;
        Trade new_order{highest.username, order.username, order.asset,
                        highest.amount, order.price};
        filled_orders.push_back({new_order});
        MakeDeposit(order.username, "USD", highest.amount * order.price);
        MakeDeposit(highest.username, order.asset, highest.amount);
        auto it = std::find(open_orders.begin(), open_orders.end(), highest);
        it->amount = 0;
      }
    }
  }
  // remove();
  if (order.amount > 0)
    conduct_chrono_trade(order);
}

void Exchange::PrintUsersOrders(std::ostream &os) const {
  os << "Users Orders (in alphabetical order):" << std::endl;
  for (auto itr = portfolio.begin(); itr != portfolio.end(); ++itr) {
    os << itr->first << "'s Open Orders (in chronological order):" << std::endl;
    for (const auto &elem : open_orders) {
      if (elem.username == itr->first)
        if (elem.amount > 0)
          os << elem.side << " " << elem.amount << " " << elem.asset << " at "
             << elem.price << " USD by " << elem.username << std::endl;
    }
    os << itr->first
       << "'s Filled Orders (in chronological order):" << std::endl;
    for (const auto &elem : filled_orders) {
      if (elem.buyer_username == itr->first) {
        if (elem.amount > 0) {
          os << "Buy " << elem.amount << " " << elem.asset << " at "
             << elem.price << " USD by " << elem.buyer_username << std::endl;
        }
      }
      if (elem.seller_username == itr->first) {
        if (elem.amount > 0) {
          os << "Sell " << elem.amount << " " << elem.asset << " at "
             << elem.price << " USD by " << elem.seller_username << std::endl;
        }
      }
    }
  }
}

void Exchange::PrintTradeHistory(std::ostream &os) const {
  os << "Trade History (in chronological order):" << std::endl;
  for (auto &elem : filled_orders) {
    if (elem.amount > 0)
      os << elem.buyer_username << " Bought " << elem.amount << " of "
         << elem.asset << " From " << elem.seller_username << " for "
         << elem.price << " USD" << std::endl;
  }
}

void Exchange::PrintBidAskSpread(std::ostream &os) const {
  std::set<std::string> unique_assets;
  for (auto &element : open_orders) {
    unique_assets.insert(element.asset);
  }
  os << "Asset Bid Ask Spread (in alphabetical order):" << std::endl;
  for (auto &elem : unique_assets) {
    int low_sell = 99999;
    int high_buy = 0;
    for (auto &elem2 : open_orders) {
      if (elem2.asset == elem) {
        if (elem2.price > high_buy && elem2.side == "Buy")
          high_buy = elem2.price;
        if (elem2.price < low_sell && elem2.side == "Sell")
          low_sell = elem2.price;
      }
    }
    os << elem << ": Highest Open Buy = ";
    if (high_buy == 0)
      os << "NA USD and ";
    else
      os << high_buy << " USD and ";
    os << "Lowest Open Sell = ";
    if (low_sell == 99999)
      os << "NA USD" << std::endl;
    else
      os << low_sell << " USD" << std::endl;
  }
}
