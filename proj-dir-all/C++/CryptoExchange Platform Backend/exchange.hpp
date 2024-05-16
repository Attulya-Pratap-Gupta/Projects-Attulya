#pragma once
#include <iostream>
#include <sstream>
#include <string>
// Added for using nested maps for easier implementation
#include <algorithm>
#include <map>
#include <vector>

#include "useraccount.hpp"
#include "utility.hpp"

class Exchange {
private:
  std::map<std::string, std::map<std::string, int>> portfolio;
  std::vector<Order> open_orders;
  std::vector<Trade> filled_orders;

public:
  void MakeDeposit(const std::string &username, const std::string &asset,
                   int amount);
  void PrintUserPortfolios(std::ostream &os) const;
  bool MakeWithdrawal(const std::string &username, const std::string &assent,
                      int amount);
  bool AddOrder(const Order &current_order);
  void PrintUsersOrders(std::ostream &os) const;
  void PrintTradeHistory(std::ostream &os) const;
  void PrintBidAskSpread(std::ostream &os) const;

  // Personally defined
  bool check_possible(const Order &pos, const std::string type);
  void buy_trade(Order order);
  void sell_trade(Order order);
  void remove();
  void conduct_chrono_trade(Order &ord);

  void sell_chrono(Order &element, Order &order);
  void buy_chrono(Order &element, Order &order);
};