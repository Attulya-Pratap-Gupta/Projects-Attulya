#pragma once
#include <iostream>
#include <string>

struct Order {
  std::string username;
  std::string side; // Can be "Buy" or "Sell"
  std::string asset;
  int amount;
  int price;

  Order() = default;

  Order(std::string u_name, std::string side_, std::string asset_, int amt,
        int rate)
      : username(u_name), side(side_), asset(asset_), amount(amt), price(rate) {
  }

  friend std::ostream &operator<<(std::ostream &os, const Order &order) {
    os << order.side << " " << order.amount << " " << order.asset << " at "
       << order.price << " USD by " << order.username << std::endl;
    return os;
  }

  bool operator==(const Order &value2) const {
    if (username == value2.username && side == value2.side &&
        asset == value2.asset && amount == value2.amount &&
        price == value2.price)
      return 1;
    return 0;
  }
};

struct Trade {
  std::string buyer_username;
  std::string seller_username;
  std::string asset;
  int amount;
  int price;
};